from npc_creator import config
import os


def plural_entity_type(entity_kind):
    return entity_kind.lower() + "s"


def entity_directory(entity_kind):
    return os.path.join(
        config.PUBLIC_ENTITY_IMAGE_PATH, plural_entity_type(entity_kind)
    )
