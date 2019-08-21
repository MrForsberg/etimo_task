import sys

import item_table
from controllers.controller import Controller


def start():
    controller = Controller()
    controller.view.print_instructions()
    choice = ''
    while choice != "Q":
        try:
            choice = input().upper()
        except KeyboardInterrupt:
            sys.exit()
        controller.handle_input(choice, list(item_table.items)[0].id)


if __name__ == '__main__':
    start()
