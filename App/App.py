from Logger.Logger import Logger
from Bd.Bd import Bd
from Bike.Bike import Bike

class App:
    logger = Logger()
    bd = Bd()

    def __init__(self):
        pass

    def main_menu(self):
        menu_option = None
        while menu_option != "5":
            print("************OPTIONS************")
            print("1. Add Bike")
            print("2. see all Bike")
            print("3. search Bike")
            print("4. delete Bike")
            print("5. exit")
            menu_option = input("Type your choose: ")

            match menu_option:
                case "1":
                    new_bike = Bike()
                    new_bike.create_bike()
                    self.bd.create_bike(new_bike)
                case "2":
                    self.bd.show_bikes()
                case "3":
                    id_search = input("Type an ID to search: ")
                    print(self.bd.search_bike(id_search))
                case "4":
                    id_search = input("Type an ID to delete: ")
                    self.bd.delete_bike(id_search)
                case "5":
                    print("Byeee!")
                case _:
                    print("opción inválida")

    def home(self):
        self.bd.create_user("admin", "12345")
        while not self.logger.isLogged:
            print("Welcome store bike")
            user = input("User: ")
            password = input("password: ")
            self.logger.loggin(user, password, self.bd)

        print("logged")
        self.main_menu()


app = App()
app.home()
