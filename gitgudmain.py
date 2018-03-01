"""hash code 2018 -- dominik branch

git gud production ;)
"""

import numpy as np

def save_file(*args):
    pass  # TODO


def open_file(filename):
    with open(filename) as file:
        w_list = file.readline().split()
        print(w_list)

        city = np.zeros([int(w_list[0]), int(w_list[1])])

        return Warehouse(
            int(w_list[0]),
            int(w_list[1]),
            int(w_list[2]),
            int(w_list[3]),
            int(w_list[4]),
            int(w_list[5])
        )

class Warehouse:
    def __init__(self, x, y, vehicle, rides, bonus, steps):
        self.vehicles = vehicle
        self.rides = rides
        self.bonus = bonus
        self.steps = steps
        self.city_x = x
        self.city_y = y

        self.city = np.zeros([x, y])


class Auto:
    def __init__(self, x, y, es, lf):
        self.start_x = x
        self.start_y = y
        self.stan = 0
        self.early_start = es
        self.latest_finish = lf
        self.points = []

def main():
    print('hello # code')
    open_file("input/a_example.in")


if __name__ == '__main__':
    main()
