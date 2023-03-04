from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column, declarative_base

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

    def image_generation_started(self):
        self.image_generator_state = 'started'

    def add_image(self, image_url):
        self.image_url = image_url
        self.image_generator_state = 'done'

    def __repr__(self):
        return f'<models.Npc id={self.id}>'

class Attribute(NpcBase):
    __tablename__ = 'attribute'

    id: Mapped[int] = Column(Integer, primary_key=True)
    npc_id: Mapped[int] = mapped_column(ForeignKey("npc.id"))
    npc: Mapped["Npc"] = relationship(back_populates="attributes")

    key: Mapped[str] = Column(String)
    value: Mapped[str] = Column(String)

    def __repr__(self):
        return f'<models.Npc id={self.id} key={self.key} value={self.value} npc_id={self.npc_id}>'
