from typing import List

import sqlalchemy
from sqlalchemy.orm import declarative_base, Session, Mapped, relationship, mapped_column
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.sql.selectable import and_

Base = declarative_base()


class Npc(Base):
    __tablename__ = 'npc'

    id: Mapped[int] = Column(Integer, primary_key=True)
    image_generator_description: Mapped[str] = Column(String)
    image_url: Mapped[str] = Column(String)
    image_generator_state: Mapped[str] = Column(String)

    attributes: Mapped[List["Attribute"]] = relationship(back_populates="npc", lazy="joined")

    def image_generation_started(self):
        self.image_generator_state = 'started'

    def add_image(self, image_url):
        self.image_url = image_url
        self.image_generator_state = 'done'


class Attribute(Base):
    __tablename__ = 'attribute'

    id: Mapped[int] = Column(Integer, primary_key=True)
    npc_id: Mapped[int] = mapped_column(ForeignKey("npc.id"))
    npc: Mapped["Npc"] = relationship(back_populates="attributes")

    key: Mapped[str] = Column(String)
    value: Mapped[str] = Column(String)


class NpcRepository:
    def __init__(self):
        file = r'C:\Users\Leto\PycharmProjects\sr_npc_creator\data\npcs.sqlite'
        self.engine = sqlalchemy.create_engine('sqlite:///' + file)
        Base.metadata.create_all(self.engine)

    def read_random(self):
        with Session(self.engine) as session:
            return session.query(Npc).order_by(func.random()).limit(1).one()

    def requires_image(self):
        filter = and_(Npc.image_generator_state.is_(None), Npc.image_url.is_(None), Npc.image_generator_description.isnot(None))
        with Session(self.engine) as session:
            return session.query(Npc).filter(filter).all()

    def find_image_description(self, beginning):
        with Session(self.engine) as session:
            return session.query(Npc).filter(Npc.image_generator_description.like(f'{beginning}%')).limit(1).one_or_none()

    def create(self, npc):
        with Session(self.engine) as session:
            session.add(npc)
            session.commit()
            return npc.id

    def save(self, npc):
        with Session(self.engine) as session:
            session.add(npc)
            session.commit()
            return npc.id


if __name__ == '__main__':
    repo = NpcRepository()

    npc = Npc(image_url='./images/Doc_Jenkins.png',
              image_generator_description='Doc Jenkins is a tall, slim man in his late 40s with short-cropped graying hair. He wears a long white lab coat and a pair of thick-rimmed glasses, and carries a large medical bag. His face is creased with worry lines, and his eyes are always darting around warily.',
              attributes=[
                  Attribute(key='Name', value='Doc Jenkins'),
                  Attribute(key='Geschlecht', value='männlich'),
                  Attribute(key='Metatyp', value='Mensch'),
                  Attribute(key='Alter', value='Mitte 40'),
                  Attribute(key='Herkunft', value='Hamburg, Deutschland')
              ]
    )

    repo.create(npc)
    npc_neu = repo.read_random()
    print(npc_neu)
