import math


class Ring:
    x = 0
    y = 0
    r = 1

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def square_found(self):
        square = math.pi * self.r ** 2
        print('Площадь = {}'.format(round(square, 2)))

    def grow(self, k):
        self.r *= k
        print('Круг увеличился в {}р., его радиус теперь = {}'.format(k, self.r))

    def intersection(self, ring2):
        cen_dist = math.sqrt((self.x - ring2.x) ** 2 + (self.y - ring2.y) ** 2)
        if not cen_dist:
            if self.r != ring2.r:
                print('Круги не пересекаются')
            else:
                print('Круги пересекаются')
        else:
            if cen_dist > self.r + ring2.r:
                print('Круги не пересекаются')
            else:
                print('Круги пересекаются')


first_ring = Ring()
second_ring = Ring(5, 5, 1)

first_ring.square_found()
first_ring.intersection(second_ring)
first_ring.grow(3)