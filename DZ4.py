class DropOf:
    def DropOff(self):
        print("Dropping off")
class Riding:
    def Ride(self):
        print("Driving")
class Truck(DropOf,Riding):
    pass
VolvoTruck = Truck()
VolvoTruck.Ride()
VolvoTruck.DropOff()