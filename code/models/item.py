from utils import Utils
import item_table


class Item(object):

    def __init__(self, name, description, units=0):
        self.id = Utils.get_unique_id()
        self.name = name
        self.description = description
        self.units = units

    def add_units(self, units):
        self.units += units

    def remove_units(self, units):
        self.units -= units

    def json(self):
        return {"id": self.id,
                "name": self.name,
                "description": self.description,
                "units": self.units}

    @classmethod
    def get_item_by_id(cls, id):
        for item in item_table.items:
            if item.id == id:
                return item
        return None
