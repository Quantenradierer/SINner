import rest_framework_simplejwt
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework.serializers import ListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
import json

from rest_framework_simplejwt.authentication import JWTAuthentication

from npc_creator import config
from npc_creator.jobs.generation_job import generation_job_async
from npc_creator.models.gpt_request import GptRequest
from npc_creator.models.image_generation import ImageGeneration
from npc_creator.operations.generate_npc import GenerateNpc
from npc_creator.repositories import npc_repo

from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from npc_creator.models import Npc
from rest_framework import serializers, viewsets

from npc_creator.services.gpt.ask_chatgpt import ask_chatgpt_moderated
from npc_creator.services.gpt_prompts import create_npc_prompt
from npc_creator.views.image import ImageSerializer


class NpcSerializer(serializers.ModelSerializer):
    attributes = serializers.DictField()
    image_objects = ListSerializer(child=ImageSerializer())
    class Meta:
        model = Npc
        fields = [field.name for field in Npc._meta.fields] + ['attributes', 'image_objects']


class NpcViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]

    queryset = Npc.objects.order_by('-id').prefetch_related().all()
    serializer_class = NpcSerializer

    def get_queryset(self):
        search_text = self.request.query_params.get('search', '')

        regex = f"(^|[^A-Za-z]){search_text}([^A-Za-z]|$)"
        return self.queryset.filter(attribute__value__regex=regex).distinct()

    @action(detail=False, methods=['get'])
    def random(self, request):
        npc = npc_repo.read_random()
        return Response(NpcSerializer(npc).data)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def prompt(self, request):
        data = json.loads(request.body.decode())
        prompt = data.get("prompt")[:255]

        serializer = self.get_serializer(data=data.get('npc', None))

        if serializer.is_valid(raise_exception=True):
            npc = Npc(attributes=serializer.validated_data['attributes'])

            result_npc = GenerateNpc(prompt, npc).call()
            if result_npc:
                return Response({'type': 'success', 'npc': NpcSerializer(result_npc.data).data})
            else:
                return Response({'type': 'error', 'error': result_npc.error})

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def save(self, request):
        data = json.loads(request.body.decode())

        serializer = self.get_serializer(data=data.get('npc', None))

        if serializer.is_valid(raise_exception=True):
            npc = Npc(attributes=serializer.validated_data['attributes'])

            if npc.is_complete():
                flagged_message = self.check_npc_content(npc)
                if flagged_message.lower() != 'ok':
                    return Response({'type': 'error', 'error': 'custom', 'message': flagged_message})

                npc.save()
                generation = ImageGeneration(npc=npc)
                generation.save()
                generation_job_async(generation)

                return Response({'type': 'success', 'npc': NpcSerializer(npc).data})
        return Response({'type': 'error', 'error': 'npc_incomplete'})

    def check_npc_content(self, npc):
        npc_prompt = create_npc_prompt(user_prompt='',
                                       npc_attributes=npc.attributes,
                                       relevant_attributes=config.RELEVANT_ATTRIBUTES)
        gpt_request = GptRequest(input=npc_prompt)
        system_prompt = '- Antworte NUR mit "Ok" oder mit einer Erklärung warum der NPC abgelehnt wurde \n- Die Attribute sollten einen NPC einen Shadowrun darstellen\n- Prüf ob die Daten inhaltlich passen\n- Verwirf Urheberrechtsverletzungen oder zu extreme Namen oder Beschreibungen\n- Der NPC sollte eine gewisse Qualität haben'
        gpt_answer = ask_chatgpt_moderated(system_prompt, gpt_request.input, 'gpt-4')
        if gpt_answer:
            gpt_request.finished(gpt_answer.data)
        else:
            gpt_request.failed()
        gpt_request.save()
        return gpt_answer.data

    @action(detail=True, methods=['post'], authentication_classes=[JWTAuthentication])
    def recreate_images(self, request, pk):
        npc = npc_repo.find(pk)
        generation = ImageGeneration(npc=npc)
        generation.save()
        generation_job_async(generation)

        return Response({'type': 'success', 'npc': NpcSerializer(npc).data})

    @action(detail=True, methods=['post'], authentication_classes=[JWTAuthentication])
    def set_default_image(self, request, pk):
        npc = npc_repo.find(pk)
        npc.default_image_number = int(request.data['image_number'])
        npc_repo.save(npc)
        return Response({'type': 'success', 'npc': NpcSerializer(npc).data})
