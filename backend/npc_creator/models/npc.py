import os
from copy import copy

from django.db import models

from npc_creator import config


class Npc(models.Model):
    class State(models.TextChoices):
        CREATED = 'CR', 'Created'
        MODERATED = 'MO', 'Moderated'
        FAILED = 'FA', 'Failed'

    state = models.CharField(
        max_length=2,
        choices=State.choices,
        default=State.CREATED,
    )

    user_prompt = models.CharField(max_length=255, blank=True)
    image_generator_description = models.TextField(blank=True)
    images = models.JSONField(default=list)

    image_generator_state = models.CharField(max_length=20, blank=True, default='init')
    default_image_number = models.IntegerField(default=0)
    max_image_number = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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

    @property
    def image_objects(self):
        return self.image_set

    def is_complete(self):
        if len([value for value in self.attributes.values() if value]) < len(config.RELEVANT_ATTRIBUTES):
            return False
        return True

    def has_image_description(self):
        return bool(self.image_generator_description)

    def __repr__(self):
        return f'<models.Npc id={self.id}>'

    def add_attributes(self, new_attributes):
        existing_attributes = self.attributes
        self.attributes = {}
        for attr_name in config.RELEVANT_ATTRIBUTES:
            value = new_attributes.get(attr_name, '') or existing_attributes.get(attr_name, '')
            self.attributes[attr_name] = value


class Attribute(models.Model):
    npc = models.ForeignKey(Npc, on_delete=models.CASCADE, db_index=True)

    key = models.TextField(db_index=True)
    value = models.TextField(db_index=True, blank=True)

    def __repr__(self):
        return f'<models.Attribute id={self.id} key={self.key} value={self.value} npc_id={self.npc_id}>'
