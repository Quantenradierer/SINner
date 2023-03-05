from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column, declarative_base

import config

NpcBase = declarative_base()
class Npc(NpcBase):
    __tablename__ = 'npc'

    id: Mapped[int] = Column(Integer, primary_key=True)
    image_generator_description: Mapped[str] = Column(String)
    image_url: Mapped[str] = Column(String)
    image_generator_state: Mapped[str] = Column(String)

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

    def get_attribute(self, name):
        return next((attr.value for attr in self.attributes if attr.key == name), None)

    def __repr__(self):
        return f'<models.Npc id={self.id}>'

    def add_attributes(self, attributes_hash):
        for attr_name in config.RELEVANT_ATTRIBUTES:
            if not self.get_attribute(attr_name):
                attribute = Attribute(key=attr_name, value=attributes_hash.get(attr_name, ''))
                self.attributes.append(attribute)


class Attribute(NpcBase):
    __tablename__ = 'attribute'

    id: Mapped[int] = Column(Integer, primary_key=True)
    npc_id: Mapped[int] = mapped_column(ForeignKey("npc.id"))
    npc: Mapped["Npc"] = relationship(back_populates="attributes")

    key: Mapped[str] = Column(String)
    value: Mapped[str] = Column(String)

    def __repr__(self):
        return f'<models.Attribute id={self.id} key={self.key} value={self.value} npc_id={self.npc_id}>'
