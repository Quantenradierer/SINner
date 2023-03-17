from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column, declarative_base

import config

NpcBase = declarative_base()


class Npc(NpcBase):
    __tablename__ = 'npc'

    id: Mapped[int] = Column(Integer, primary_key=True)
    user_prompt: Mapped[str] = Column(String)
    image_generator_description: Mapped[str] = Column(String)
    image_url: Mapped[str] = Column(String)
    image_generator_state: Mapped[str] = Column(String)  # None, 'started', 'done', 'failed', 'banned'

    attributes: Mapped[List["Attribute"]] = relationship(back_populates="npc",
                                                         lazy="joined",
                                                         cascade="all, delete-orphan")

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
        self.image_generator_description = None
        attribute = self.get_attribute(config.VISUAL_APPEARANCE_ATTRIBUTE)
        if attribute:
            self.attributes.remove(attribute)

    def get_attribute(self, name):
        return next((attr.value for attr in self.attributes if attr.key == name), None)

    def __repr__(self):
        return f'<models.Npc id={self.id}>'

    def add_attributes(self, attributes_hash):
        for attr_name in config.RELEVANT_ATTRIBUTES:
            if not self.get_attribute(attr_name):
                attribute = Attribute(key=attr_name, value=attributes_hash.get(attr_name, ''))
                self.attributes.append(attribute)

    def requires_image_generation(self):
        return all([
            self.image_generator_state is None,
            self.image_url is None,
            self.image_generator_description is not None
        ])

    def requires_image_download(self):
        return self.image_generator_state == 'started' and self.image_url is None

    def requires_new_image_generator_description(self):
        return self.image_generator_description is None or self.image_generator_state in ['failed', 'banned']

class Attribute(NpcBase):
    __tablename__ = 'attribute'

    id: Mapped[int] = Column(Integer, primary_key=True)
    npc_id: Mapped[int] = mapped_column(ForeignKey("npc.id"))
    npc: Mapped["Npc"] = relationship(back_populates="attributes")

    key: Mapped[str] = Column(String)
    value: Mapped[str] = Column(String)

    def __repr__(self):
        return f'<models.Attribute id={self.id} key={self.key} value={self.value} npc_id={self.npc_id}>'
