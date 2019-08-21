import sys

from views.view import View
from controllers.item_controller import ItemController


class Controller(object):

    def __init__(self):
        self.view = View()
        self.item_controller = ItemController()

    def handle_input(self, input, id):
        try:
            input_action = input[0]
            input_number = input[1:]
        except IndexError:
            self.view.show_invalid_input()
            return
        if (input_action == "Q"):
            sys.exit()
        elif(input_action == "S" and input_number.isdigit()):
            response = self.item_controller.remove_units(id, input_number)
            self.view.item_units_has_changed(response)
        elif(input_action == "I" and input_number.isdigit()):
            response = self.item_controller.add_units(id, input_number)
            self.view.item_units_has_changed(response)
        elif(input_action == "L" and not input_number):
            response = self.item_controller.get_item_by_id(id)
            self.view.show_item_information(response)
        else:
            self.view.show_invalid_input()
