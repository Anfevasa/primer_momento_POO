class Bd:
    users = {}
    bikes = {}

    def __init__(self):
        pass

    def create_user(self, user, password):
        self.users[user] = password
        print("User created")

    def check_user(self, user, password):
        return self.users[user] == password

    def create_bike(self,bike):
        self.bikes[bike.id] = bike.dict_bike()
        print("Bike created")


    def show_bikes(self):
        for bike in self.bikes:
            print(self.bikes[bike])

    def search_bike(self,id):
        return  self.bikes[id]

    def delete_bike(self,id):
        self.bikes.pop(id)
        print("Eliminado")