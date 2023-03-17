from flask import Flask, request
from flask_cors import CORS

from models.npc import Npc
from operations.generate_npc import GenerateNpc
from repositories.npc import NpcRepository

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

npc_repo = NpcRepository()


def convert_npc(npc):
    attributes_dict = {}
    for attribute in npc.attributes:
        attributes_dict[attribute.key] = attribute.value

    npc_dict = {c.name: getattr(npc, c.name) for c in npc.__table__.columns}
    return {**npc_dict, **{'attributes': attributes_dict}}


@app.route('/api/npc/<id>', methods=['GET'])
@app.route('/api/npc/', methods=['GET'])
def read_npc(id=None):
    if id and id.isdigit():
        npc = npc_repo.find(id)
    else:
        npc = npc_repo.read_random()

    return convert_npc(npc)


@app.route('/api/npc', methods=['POST'])
def create_npc():
    prompt = request.json['prompt'][:255]

    result_npc = GenerateNpc(prompt).call()
    if result_npc:
        npc = result_npc.data
    else:
        npc = Npc(id='error', attributes={'Name': result_npc.error})

    return convert_npc(npc)

if __name__ == '__main__':
    app.run()
