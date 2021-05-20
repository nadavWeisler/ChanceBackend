from UserService import User


class Project:
    """
    this is a project which has all the details about specific project
    """
    def __init__(self, employer, programmer):
        self.employer = employer
        self.progammer = programmer
