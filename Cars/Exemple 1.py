class Car:
    def __init__(self):
        self.fuel = 100
        self.mileage = 0
        self.engine_on = False

    def start(self):
        self.engine_on = self.fuel > 0

    def drive(self, distance):
        if self.engine_on and self.fuel >= distance * 0.05:
            self.fuel -= distance * 0.05 #F=2.5 #F=5
            self.mileage += distance

    def refuel(self, amount):
        self.fuel += amount

if __name__ == '__main__':
    car = Car()
    car.start()
    car.drive(50) #100-2.5=97.5
    car.refuel(20) #97.5+20=117.5
    car.drive(100) #117.5-5=112.5
    # la voiture a conduit 150 kilomètres au total (50 + 100)
    print(f"Mileage: {car.mileage}, Fuel: {car.fuel}")
#Représente une voiture avec trois attributs : fuel (carburant), mileage (kilométrage) et engine_on (état du moteur).
