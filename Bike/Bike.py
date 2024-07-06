class Bike:
    def __init__(self):
        pass

    def create_bike(self):
        self.id = input("ID Bike: ")
        self.brand = input("brand: ")
        self.ref = input("ref: ")
        self.year = input("year: ")

    def dict_bike(self):
        return {
            "id":self.id,
            "brand":self.brand,
            "ref":self.ref,
            "year":self.year
        }