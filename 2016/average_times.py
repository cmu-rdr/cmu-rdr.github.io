#!/usr/bin/env python

import fileinput

def convert_to_millis(timeval):
    minutes,seconds,tenths = timeval.split(':')
    minutes = int(minutes) * 60 * 1000
    seconds = int(seconds) * 1000
    tenths = int(tenths) * 10
    return minutes + seconds + tenths

def convert_to_tuple(millis):
    millis = int(millis)
    minutes = millis / (60 * 1000)
    millis = millis - (minutes * 60 * 1000)
    seconds = millis / 1000
    millis = millis - seconds * 1000
    tenths = millis / 10
    millis  = millis - tenths * 10
    return (minutes, seconds, tenths)

# Source:
#       http://docs.python.org/tutorial/stdlib.html#quality-control
def average(values):
    return sum(values, 0.0) / float(len(values))

if __name__ == '__main__':
    for line in fileinput.input():
        space_split = line.split()
        #print '%s -- %s' % (space_split[0], space_split[1])
        time1 = convert_to_millis(space_split[0])
        time2 = convert_to_millis(space_split[1])
        print '%d:%0.2d:%0.2d' % (convert_to_tuple(average([time1,time2])))

