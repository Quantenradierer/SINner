from functools import cache

import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.selectable import and_

import config
from models.npc import Npc, NpcBase


class NpcRepository:
    # Borg Pattern to avoid additional connections: https://code.activestate.com/recipes/66531/
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

        if not hasattr(self, 'engine'):
            self.engine = sqlalchemy.create_engine('sqlite:///' + config.SQLITE_FILE)
            NpcBase.metadata.create_all(self.engine)

    def read_random(self):
        with Session(self.engine) as session:
            return session.query(Npc).order_by(func.random()).limit(1).one()

    def find(self, id):
        with Session(self.engine) as session:
            return session.query(Npc).filter_by(id=id).limit(1).one()

    def requires_image_generation(self):
        filter = and_(Npc.image_generator_state.is_(None), Npc.image_url.is_(None),
                      Npc.image_generator_description.isnot(None))
        with Session(self.engine) as session:
            return session.query(Npc).filter(filter).all()

    def requires_image_download(self):
        filter = and_(Npc.image_generator_state.is_('started'), Npc.image_url.is_(None))
        with Session(self.engine) as session:
            return session.query(Npc).filter(filter).all()

    def find_image_description(self, beginning):
        with Session(self.engine) as session:
            return session.query(Npc).filter(
                Npc.image_generator_description.like(f'{beginning}%')).limit(1).one_or_none()

    def create(self, npc):
        with Session(self.engine) as session:
            session.add(npc)
            session.commit()
            return npc.id

    def delete(self, npc):
        with Session(self.engine) as session:
            session.delete(npc)
            session.commit()
            return npc.id

    def save(self, npc):
        with Session(self.engine) as session:
            session.add(npc)
            session.commit()
            return npc.id

    def close(self):
        self.engine.dispose(close=True)
        del self.engine
