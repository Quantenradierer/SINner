def find_correct_key(used_attribute_keys: list[str], key: str):
    """
    Sometimes GPT does not answer with the correct key, but removes part of it
    Like "Glück (1-6)" will be reduced to "Glück". In order to find it, we just look at the start of the keys.
    But "Stärke" shouldn't match with "Stärken".
    """
    for used_key in used_attribute_keys:
        if used_key.split(" ")[0].upper() == key.upper():
            return used_key
    return key


def dict_from_text(used_attribute_keys: list[str], text: str):
    lines = text.split("\n")

    attributes = {}
    for line in lines:
        if ":" not in line:
            continue

        splitted = line.split(":")
        key, value = splitted[0], "".join(splitted[1:])
        key = key.strip()

        if key not in used_attribute_keys:
            key = find_correct_key(used_attribute_keys, key)

        if key not in used_attribute_keys:
            continue
        attributes[key] = value.strip()

    return attributes
