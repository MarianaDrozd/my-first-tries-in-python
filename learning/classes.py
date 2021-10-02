from collections import namedtuple


class Goat:
    legs_number = 4

    def __init__(self, height, weight, horns):
        self.height = height
        self.weight = weight
        self.horns = horns

    def __str__(self):
        s = "height = {}, weight = {}, horns = {}".format(self.height, self.weight, self.horns)
        return s


marusya = Goat(60, 40, 2)


notka = Goat(65, 42, 1)
for x in notka, marusya:
    print(x)
notka.weight += 1
x = notka
x.height += 5
marusya.height += 10
print(notka, marusya)


class Empty:
    pass


Point = namedtuple("Point", "x y z")
A = Point(1, 0, 3)
print(A.x)
