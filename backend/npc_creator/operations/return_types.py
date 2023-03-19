

class ReturnType:
    pass


class Failure(ReturnType):
    def __init__(self, error):
        self.error = error

    def __bool__(self):
        return False

    def __repr__(self):
        return f'<Failure: error: {self.error}>'


class Success(ReturnType):
    def __init__(self, data=None):
        self.data = data

    def __bool__(self):
        return True
