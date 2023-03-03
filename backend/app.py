from flask import Flask
from flask_cors import CORS

from backend.repositories.npc import NpcRepository


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

npc_repo = NpcRepository()


@app.route('/npc')
def npc():
    npc = npc_repo.read_random()
    attributes_dict = {}
    for attribute in npc.attributes:
        attributes_dict[attribute.key] = attribute.value

    npc_dict = {c.name: getattr(npc, c.name) for c in npc.__table__.columns}
    return {**npc_dict, **{'attributes': attributes_dict}}


if __name__ == '__main__':
    app.run()
