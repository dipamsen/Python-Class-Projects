# Object Oriented Programming

class Car():
    def __init__(self, model, color, company, speedlimit):
        self.model = model
        self.color = color
        self.company = company
        self.speedlimit = speedlimit
        self.moving = False

    def start(self):
        if(self.moving == True):
            print("Car is already moving!")
        else:
            print("Car started")
            self.moving = True

    def stop(self):
        if(self.moving == False):
            print("Car is not moving!")
        else:
            self.moving = False
            print("Car Stopped")

    def accelerate(self):
        if(self.moving == False):
            print("Car is not moving!")
        else:
            print("Accelerated car")


car1 = Car("ABC123", "red", "audi", 10)
print(car1.color)
print(car1.moving)
car1.start()
print(car1.moving)
car1.accelerate()
print(car1.moving)
car1.stop()
print(car1.moving)
