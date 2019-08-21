

class View(object):

    def print_instructions(self):
        print("****************************************")
        print("S + nummer för att sälja artiklar")
        print("I + nummer för att inleverera artiklar")
        print("L för att se lagersaldo")
        print("****************************************")

    def show_item_information(self, response):
        print("****************************************")
        if(response["status"] == 200):
            item = response.get("data")
            print("ID: {0}".format(item.get("id")))
            print("Namn: {0}".format(item.get("name")))
            print("Beskrivning: {0}".format(item.get("description")))
            print("Antal i lager: {0}".format(str(item.get("units"))))
        else:
            print(response.message)
        print("****************************************")

    def show_invalid_input(self):
        print("Felaktigt input")
        self.print_instructions()

    def item_units_has_changed(self, response):
        print("****************************************")
        print(response["message"])
        print("****************************************")
