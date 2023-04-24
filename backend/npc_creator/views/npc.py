import rest_framework_simplejwt
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
import json

from rest_framework_simplejwt.authentication import JWTAuthentication

from npc_creator.operations.generate_npc import GenerateNpc
from npc_creator.operations.recreate_image import RecreateImage
from npc_creator.repositories import npc_repo

from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from npc_creator.models import Npc
from rest_framework import serializers, viewsets


class NpcSerializer(serializers.ModelSerializer):
    attributes = serializers.DictField()
    class Meta:
        model = Npc
        fields = [field.name for field in Npc._meta.fields] + ['attributes']


class NpcViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]

    queryset = Npc.objects.order_by('-id').prefetch_related().all()
    serializer_class = NpcSerializer

    def get_queryset(self):
        search_text = self.request.query_params.get('search', '')
        moderated = self.request.query_params.get('moderated', '') == 'on'

        states = [Npc.State.MODERATED]
        if not moderated:
            states.append(Npc.State.CREATED)

        return self.queryset.filter(attribute__value__icontains=search_text, state__in=states).distinct()

    @action(detail=False, methods=['get'])
    def random(self, request):
        npc = npc_repo.read_random()
        return Response(convert_npc(npc))

    @csrf_exempt
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def prompt(self, request):
        data = json.loads(request.body.decode())
        prompt = data.get("prompt")[:255]

        result_npc = GenerateNpc(prompt).call()
        if result_npc:
            return Response({'type': 'success', 'id': result_npc.data.id})
        else:
            return Response({'type': 'error', 'error': result_npc.error})

    @action(detail=True, methods=['post'], authentication_classes=[JWTAuthentication])
    def recreate_images(self, request, pk):
        npc = npc_repo.find(pk)
        result = RecreateImage(npc).call()
        if result:
            return Response({'type': 'success', 'npc': convert_npc(npc)})
        else:
            return Response({'type': 'error', 'error': result.error})

    @action(detail=True, methods=['post'], authentication_classes=[JWTAuthentication])
    def set_default_image(self, request, pk):
        npc = npc_repo.find(pk)
        npc.default_image_number = int(request.data['image_number'])
        npc_repo.save(npc)
        return Response({'type': 'success', 'npc': convert_npc(npc)})


def convert_npc(npc):
    return {
        'id': npc.id,
        'image_generator_description': npc.image_generator_description,
        'image_url': npc.image_url,
        'image_generator_state': npc.image_generator_state,
        'attributes': npc.attributes,
        'default_image_number': npc.default_image_number,
        'max_image_number': npc.max_image_number,
        'state': npc.state,
        'user_prompt': npc.user_prompt

    }