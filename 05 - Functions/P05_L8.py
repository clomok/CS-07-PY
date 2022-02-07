class Car:
    def __init__(self, colorinput, windowsinput, priceinput):
        self.color = colorinput
        self.windows = windowsinput
        self.price = priceinput

car1 = Car("Red", 4, 10000)
car2 = Car("Blue", 2, 300500)

print(car1.color)
print(car2.price)