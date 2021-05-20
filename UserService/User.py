import flask_user


class User:
    def __init__(self, kind):
        self.rank = 0  # total rank by past projets
        self.kind = kind  # publisher of programmer
        # todo more properties to the user
