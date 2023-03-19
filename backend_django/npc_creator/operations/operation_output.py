

class Failure:
    def __init__(self, error):
        self.error = error

    def __bool__(self):
        return False

    def __repr__(self):
        return f'<Failure: error: {self.error}>'


class Success:
    def __init__(self, data=None):
        self.data = data

    def __bool__(self):
        return True