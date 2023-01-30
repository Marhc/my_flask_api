from util.classes import DictController
from util.functions import filename

resource_name = filename(__file__)


class UserController(DictController):
    def __init__(self):
        super().__init__(resource_name)
