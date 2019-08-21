from models.item import Item
from utils import Utils
import const


class ItemController(object):

    def add_units(self, id, units):
        item = Item.get_item_by_id(id)
        if (item is None):
            return Utils.create_response_message(
                         const.ITEM_NOT_FOUND, 404)
        try:
            number_of_units = int(units)
        except ValueError:
            return Utils.create_response_message(
                         const.ITEM_DEFAULT_ADD_ERROR, 500)
        if(number_of_units == 0):
            return Utils.create_response_message(
                         const.ITEM_ZERO_UNITS_ADD_ERROR, 403)
        units_before = item.units
        item.add_units(number_of_units)
        if((units_before + number_of_units) != item.units):
            return Utils.create_response_message(
                         const.ITEM_DEFAULT_ADD_ERROR, 500)
        if(number_of_units == 1):
                return Utils.create_response_message(
                             const.ITEM_ADD_SINGLE_SUCCESS.format(number_of_units), 201)
        return Utils.create_response_message(
                     const.ITEM_ADD_MULTIPLE_SUCCESS.format(number_of_units), 201)

    def remove_units(self, id, units):
        item = Item.get_item_by_id(id)
        if (item is None):
            return Utils.create_response_message(
                         const.ITEM_NOT_FOUND, 404)
        try:
            number_of_units = int(units)
        except ValueError:
            return Utils.create_response_message(
                         const.ITEM_DEFAULT_ADD_ERROR, 500)
        if(number_of_units == 0):
            return Utils.create_response_message(
                         const.ITEM_ZERO_UNITS_REMOVE_ERROR, 405)
        if ((item.units - number_of_units) < 0):
            return Utils.create_response_message(
                        const.ITEM_NEGATIVE_VALUE_REMOVE_ERROR, 405)
        units_before = item.units
        item.remove_units(number_of_units)
        if((units_before - number_of_units) != item.units):
            return Utils.create_response_message(
                         const.ITEM_DEFAULT_REMOVE_ERROR, 500)
        if (number_of_units == 1):
            return Utils.create_response_message(const.ITEM_REMOVE_SINGLE_SUCCESS
                                                 .format(number_of_units), 200)
        return Utils.create_response_message(const.ITEM_REMOVE_MULTIPLE_SUCCESS
                                             .format(number_of_units), 200)

    def get_item_by_id(self, id):
        item = Item.get_item_by_id(id)
        if (item is None):
            return Utils.create_response_message(
                         const.ITEM_NOT_FOUND, 404)
        return Utils.create_response_data(item.json(), 200)
