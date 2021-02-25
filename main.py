#!/usr/bin/env python3
import sys

def get_input(filepath):
    counter = 0
    file = open(filepath, 'r')
    content = file.readlines()
    new = []
    for lines in content:
        new.append(lines.split(" "))
        new[counter] = lines.rstrip()
        counter += 1
    firstline = []
    streets = []
    cars = []
    firstline.append(new[0])

    stop = 0
    counter_for_cars = 0
    for x in new:
        if stop == 0:
            stop +=1
            continue
        tmp = x[::-1][0]
        if tmp.isnumeric() == True:
            streets.append(x)
            counter_for_cars += 1
    stop = 0
    for x in new:
        if stop <= counter_for_cars:
            stop +=1
            continue
        cars.append(x)

    file.close()
    print(firstline)
    print(streets)
    print(cars)
    return firstline, streets, cars


def loop(coll):
    intersections = 0

    for i in range(2):
        print("works")
        

def main(argv):
    coll = get_input(argv[1])
    loop(coll)





if __name__ == '__main__':
    main(sys.argv)
