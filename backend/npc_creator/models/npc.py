from copy import copy

from django.db import models

from npc_creator import config


class Npc(models.Model):
    class State(models.TextChoices):
        CREATED = 'CR', 'Created'
        MODERATED = 'MO', 'Moderated'

    state = models.CharField(
        max_length=2,
        choices=State.choices,
        default=State.CREATED,
    )

    user_prompt = models.CharField(max_length=255, blank=True)
    image_generator_description = models.TextField(blank=True)
    image_url = models.CharField(max_length=255, blank=True)
    image_generator_state = models.CharField(max_length=20, blank=True, default='init')

    def __init__(self, *args, **kwargs):
        self.attributes = {}
        attributes = kwargs.pop('attributes', {})
        super(Npc, self).__init__(*args, **kwargs)
        if self.id:
            self.attributes = dict([(attr.key, attr.value) for attr in self.attribute_set.all()])
        self.add_attributes(attributes)

    def save(self, *args, **kwargs):
        super(Npc, self).save(*args, **kwargs)

        attribute_set = self.attribute_set.all()
        attributes_hash = copy(self.attributes)
        for attribute in attribute_set:
            if attribute.key in attributes_hash:
                attribute.value = attributes_hash[attribute.key]
                attribute.save()
                attributes_hash.pop(attribute.key)
            else:
                attribute.delete()

        for key, value in attributes_hash.items():
            attribute = Attribute(key=key, value=value, npc=self)
            attribute.save()

    def has_image_description(self):
        return bool(self.image_generator_description)

    def image_generation_started(self):
        self.image_generator_state = 'started'

    def add_image(self, image_url):
        self.image_url = image_url
        self.image_generator_state = 'done'

    def image_generation_failed(self):
        self.image_generator_state = 'failed'

    def image_generation_used_banned_word(self):
        self.image_generator_state = 'banned'

    def __repr__(self):
        return f'<models.Npc id={self.id}>'

    def add_attributes(self, new_attributes):
        existing_attributes = self.attributes
        self.attributes = {}
        for attr_name in config.RELEVANT_ATTRIBUTES:
            value = new_attributes.get(attr_name, '') or existing_attributes.get(attr_name, '')
            self.attributes[attr_name] = value

    def requires_image_generation(self):
        return self.image_generator_state in ['init', 'banned'] and self.image_generator_description and not self.image_url.strip()

    def requires_image_download(self):
        return self.image_generator_state in ['started', 'failed'] and not self.image_url

    def requires_new_image_generator_description(self):
        return not self.image_generator_description or self.image_generator_state in ['failed', 'banned']

    def reset_image(self):
        self.image_url = ''
        self.image_generator_state = 'init'
        self.image_generator_description = ''
        self.attributes[config.VISUAL_APPEARANCE_ATTRIBUTE] = ''

class Attribute(models.Model):
    npc = models.ForeignKey(Npc, on_delete=models.CASCADE, db_index=True)

    key = models.TextField(db_index=True)
    value = models.TextField(db_index=True, blank=True)

    def __repr__(self):
        return f'<models.Attribute id={self.id} key={self.key} value={self.value} npc_id={self.npc_id}>'
