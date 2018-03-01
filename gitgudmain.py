"""hash code 2018 -- dominik branch

git gud production ;)
"""

#import numpy as np


def save_file(*args):
    pass  # TODO


def open_file(filename):
    with open(filename) as file:
        w_list = file.readline().split()
        print(w_list)

        auto_list = []
        for line in file:
            al = line.split()
            auto_list.append(
                Ride(
                    int(al[0]),
                    int(al[1]),
                    int(al[2]),
                    int(al[3]),
                    int(al[4]),
                    int(al[5])
                ))

        for car in auto_list:
            print(car)
        autolist = auto_list.sort(key=lambda x: int(x.early_start))
        return Warehouse(
            int(w_list[0]),
            int(w_list[1]),
            int(w_list[2]),
            int(w_list[3]),
            int(w_list[4]),
            int(w_list[5]),
            autolist
        )


class Warehouse:
    def __init__(self, x, y, vehicle, rides, bonus, steps, objrides):
        self.vehicles = vehicle
        self.rides = rides #all ride to do
        self.bonus = bonus
        self.steps = steps
        self.city_x = x
        self.city_y = y

        self.av_cars = []
        for i in range(vehicle):
            self.av_cars.append(Auto(i, 0, 0, None))

        self.rides_obj = []


        #self.city = np.zeros([x, y])


class Ride: # raidy tak naprawde
    def __init__(self, x, y, fx, fy, es, lf):
        self.start = [x, y]
        self.finish = [fx, fy]
        self.stan = 0
        self.early_start = es
        self.latest_finish = lf
        self.points = []

    def __str__(self):
        return str(self.start) \
               + ' ' + str(self.finish) \
               + ' ' + str(self.early_start) \
               + ' ' + str(self.latest_finish)

class Auto:
    def __init__(self, id,  x , y, ride):

        self.id = id
        self.position = [x, y]
        self.flag = 0

        self.start_queue = []
        self.finish_queue = []

        self.ride = ride

def main():
    print('hello # code')
    w = open_file("input/a_example.in")

    for T in range(0, w.steps):

        print(w.rides_obj)
        r = w.rides_obj[0]
        for ride in w.rides_obj:
            if r.early_start > ride.early_start:
                r = ride

        for auto in w.av_cars:
            if auto.ride is None:
                auto.ride = r

                in_x = []

                temp = auto.position
                for i in range(0, abs(auto.position[0] - auto.ride.start[0])):
                    temp[0] = temp[0] + 1
                    in_x.append([temp[0],temp[1]])

                for j in range(0, abs(temp[1] - auto.ride.start[1])):
                    temp[1] = temp[1] + 1
                    in_x.append([temp[0], temp[1]])

                auto.start_queue = in_x
                print(in_x)

                break


        '''for auto in w.av_cars:
            if auto.ride is not None:
                if'''





if __name__ == '__main__':
    main()
