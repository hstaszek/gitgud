"""hash code 2018 -- dominik branch

git gud production ;)
"""

#import numpy as np
import time

def save_file(w):
    with open('fff.out', 'w') as file:
        for car in w.av_cars:
            s = ''.join(str(car.assigned_raids))
            s = str(len(car.assigned_raids)) + ' ' + s
            file.write(s)
            file.write('\n')


def open_file(filename):
    with open(filename) as file:
        w_list = file.readline().split()
        #print(w_list)


        countr = 0
        auto_list = []
        for line in file:
            al = line.split()
            auto_list.append(
                Ride(
                    countr,
                    int(al[0]),
                    int(al[1]),
                    int(al[2]),
                    int(al[3]),
                    int(al[4]),
                    int(al[5])
                ))
            countr += 1

        auto_list.sort(key=lambda x: x.early_start)
        #for car in auto_list:
            #print(car)

        return Warehouse(
            int(w_list[0]),
            int(w_list[1]),
            int(w_list[2]),
            int(w_list[3]),
            int(w_list[4]),
            int(w_list[5]),
            auto_list
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
            self.av_cars.append(Auto(i+1, 0, 0, None))

        self.rides_obj = []
        self.rides_obj = objrides


        #self.city = np.zeros([x, y])


class Ride: # raidy tak naprawde
    def __init__(self,id, x, y, fx, fy, es, lf):
        self.ride_id = id

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

        self.assigned_raids = []

        self.ride = ride


def main():

    start_time = time.time()
    print('hello # code')
    w = open_file("input/e_high_bonus.in")

    for T in range(0, w.steps):

        #print(T, 'simulation Step')

        for auto in w.av_cars:
            if len(w.rides_obj) != 0:

                if auto.ride is None:
                    auto.ride = w.rides_obj[0]
                    auto.assigned_raids.append(w.rides_obj[0].ride_id)
                    w.rides_obj.pop(0)

                    in_x = []
                    count = 1
                    if auto.position[0] - auto.ride.start[0] > 0:
                        count = -1

                    temp = auto.position
                    for i in range(0, abs(auto.position[0] - auto.ride.start[0])):
                        temp[0] = temp[0] + count
                        in_x.append([temp[0], temp[1]])

                    count = 1
                    if temp[1] - auto.ride.start[1] > 0:
                        count = -1

                    for j in range(0, abs(temp[1] - auto.ride.start[1])):
                        temp[1] = temp[1] + count
                        in_x.append([temp[0], temp[1]])

                    auto.start_queue = in_x
                    #print(in_x)


                    in_x = []
                    count = 1
                    if temp[0] - auto.ride.finish[0] > 0:
                        count = -1

                    for i in range(0, abs(temp[0] - auto.ride.finish[0])):
                        temp[0] = temp[0] + count
                        in_x.append([temp[0], temp[1]])

                    count = 1
                    if temp[1] - auto.ride.finish[1] > 0:
                        count = -1

                    for j in range(0, abs(temp[1] - auto.ride.finish[1])):
                        temp[1] = temp[1] + count
                        in_x.append([temp[0], temp[1]])

                    auto.finish_queue = in_x

                    #print(in_x)

        for car in w.av_cars:
            if car.ride is not None:
                if len(car.start_queue) is not 0:
                    car.position = car.start_queue[0]
                    car.start_queue.pop(0)
                elif len(car.finish_queue) is not 0:
                    car.position = car.finish_queue[0]
                    car.finish_queue.pop(0)
                else:
                    car.ride = None

                #print(car.position)

    save_file(w)
    print("--- %s seconds ---" % (time.time() - start_time))



if __name__ == '__main__':
    main()
