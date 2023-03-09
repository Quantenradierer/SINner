from flask import Flask, request
from flask_cors import CORS

from operations.generate_npc import generate_npc
from repositories.npc import NpcRepository


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

npc_repo = NpcRepository()


@app.route('/npc/<id>', methods=['GET'])
@app.route('/npc/', methods=['GET'])
def read_npc(id=None):
    if id and id.isdigit():
        npc = npc_repo.find(id)
    else:
        npc = npc_repo.read_random()

    attributes_dict = {}
    for attribute in npc.attributes:
        attributes_dict[attribute.key] = attribute.value

    npc_dict = {c.name: getattr(npc, c.name) for c in npc.__table__.columns}
    return {**npc_dict, **{'attributes': attributes_dict}}


@app.route('/npc', methods=['POST'])
def create_npc():
    prompt = request.json['prompt'][:255]
    
    npc = generate_npc(prompt)

    attributes_dict = {}
    for attribute in npc.attributes:
        attributes_dict[attribute.key] = attribute.value

    npc_dict = {c.name: getattr(npc, c.name) for c in npc.__table__.columns}
    return {**npc_dict, **{'attributes': attributes_dict}}


if __name__ == '__main__':
    app.run()
