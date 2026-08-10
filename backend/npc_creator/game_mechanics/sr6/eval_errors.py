class NotExistingAttributeError(Exception):
    """
    raised, when an attribute is accessed that does not exist
    e.g. character.current_armor but the character got no current armor
    it indicates that nothing can be calculated, so it's just ignored
    """

    pass
