from util.classes import DictController


class UserController(DictController):
    def __init__(self):
        resource = 'users'
        super().__init__(resource)
