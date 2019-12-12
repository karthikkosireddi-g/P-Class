class aCar:
    cMake = ""
    cModel = ""
    cYear = ""

    def driveCar(self, car):
        print("Driving ", car)

    def parkCar(self, car):
        print("Parking ", car)

car1 = aCar()
car1.cMake = "Porsche"
car1.cModel = "911"
car1.cYear = "2001"

print(car1.cMake)
car1.driveCar(car1.cMake)
car1.parkCar(car1.cMake)

car2 = aCar()
car2.cMake = "Lambo"
car2.cModel = "Avent"
car2.cYear = "2019"

print(car2.cMake)
car2.driveCar(car2.cMake)
car2.parkCar(car2.cMake)
