#Fernando Guzman
#03/02/25

#Modify original code to add two additional attributes

class car:

    def __init__(self, manufacturer, model, car_type, year, color):
        self.manufacturer = manufacturer
        self.model = model
        self.car_type = car_type
        self.year = year
        self.color = color

    def get_manufacturer(self):
        return self.manufacturer
    
    def get_model(self):
        return self.model

    def get_car_type(self):
        return self.car_type

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def fullspecs(self):
        return self.manufacturer + " " + self.model + " " + self.car_type + " " + str(self.year) + " " + self.color

car1 = car("Chevorlet", "Camaro", "Sports", 2012, "Blue")
car2 = car("Toyota", "Camry", "Sedan" , 2020, "Black")

print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car2.get_model())
print(car1.fullspecs())
print(car2.fullspecs())
