from repositories.npc import NpcRepository

repo = NpcRepository()


def switch_ids(from_id, to_id):
    """
    yep, the only purpose for this script is to move myself to id=1
    did you know, all from npc.id = 1 was created by GPT3, except the name?
    """
    try:
        repo.find(to_id)
        raise Exception(f'ID {to_id} is already used! Please choose another one!')
    except:
        pass

    npc = repo.find(from_id)
    npc.id = to_id
    for attribute in npc.attributes:
        attribute.npc_id = to_id
    repo.save(npc)


if __name__ == '__main__':
    switch_ids(1, 83)
    switch_ids(82, 1)