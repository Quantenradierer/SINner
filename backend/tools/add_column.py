from sqlalchemy import Column, String, text

from repositories.npc import NpcRepository


def add_column(engine, table_name, column):
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)
    with engine.connect() as con:
        con.execute(text('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type)))


if __name__ == '__main__':
    repo = NpcRepository()

    column = Column('user_prompt', String(255))
    add_column(repo.engine, 'npc', column)
