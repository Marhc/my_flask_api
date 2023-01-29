from database.dict_db import db
from util.validation import if_exists, serialize


class DictController:
    def __init__(self, resource):
        self.table = db[resource]
        self.resource = resource

    def create(self, data):
        item = {
            "id": len(self.table) + 1,
            **data
        }

        self.table.append(item)

        response = serialize(self.resource, item)

        return response, 201

    @if_exists
    def read(self, index):
        item = self.table[index]

        return serialize(self.resource, item)

    @if_exists
    def update(self, index, data):
        self.table[index].update(data)

        item = self.table[index]

        return serialize(self.resource, item)

    @if_exists
    def delete(self, index):
        del self.table[index]

        return '', 204

    def list(self):
        return serialize(self.resource, self.table, many=True)
