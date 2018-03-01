"""hash code 2018 -- dominik branch

git gud production ;)
"""

import numpy as np

def save_file(*args):
    pass  # TODO


def open_file(filename):
    with open(filename) as file:
        warehoouse_list = file.readline().split()
        print(warehoouse_list)

        city = np.zeros([])

        return Warehouse()

class Warehouse:
    def __init__(self, cityx, cityy, vehicle, rides, bonus, steps):
        self.vehicles = vehicle
        self.rides = rides
        self.bonus = bonus
        self.steps = steps



def main():
    print('hello # code')
    open_file("input/a_example.in")


if __name__ == '__main__':
    main()
