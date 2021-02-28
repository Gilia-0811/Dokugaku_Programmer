# http://tinyurl.com/hz9qdh3

class Horse() :
    def __init__(self, name, rider) :
        self.name = name
        self.rider = rider

class Rider() :
    def __init__(self, name) :
        self.name = name

a_rider = Rider("Gilia")
a_horse = Horse("Python", a_rider)

print("The name of Horse is {}".format(a_horse.name))
print("The name of Rider is {}".format(a_horse.rider.name))
