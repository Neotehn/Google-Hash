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

    firstline.append(new[0].split(" "))

    stop = 0
    counter_for_cars = 0
    for x in new:
        if stop == 0:
            stop +=1
            continue
        tmp = x[::-1][0]
        if tmp.isnumeric() == True:
            streets.append(x.split(" "))
            counter_for_cars += 1
    stop = 0
    for x in new:
        if stop <= counter_for_cars:
            stop +=1
            continue
        cars.append(x.split(" "))

    file.close()
    return firstline, streets, cars


def sort_len(elem):
    return len(elem)

def loop(coll):
    intersections = 0

    coll[2].sort(key=sort_len)
    for i in range(int(coll[0][0][0])):
        
        

def main(argv):
    coll = get_input(argv[1])
    loop(coll)





if __name__ == '__main__':
    main(sys.argv)
