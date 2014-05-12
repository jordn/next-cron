#!/usr/bin/python

import os, argparse
from sys import stdin
import datetime
import fileinput

def main(args):
    print 'Input file is', args.input

time_mins, time_hours = 46, 0 
start_time = datetime.datetime.now().replace(hour=time_hours, minute=time_mins)
print start_time
print "Start time: {0:%H}:{0:%M} {1}".format(start_time, "today")


for line in fileinput.input():
    mins, hours, program = line.strip().split(' ')
    if hours == '*':
        if mins == '*' or int(mins) > start_time.minute:
            hours = time_hours
        else:
            hours = time_hours + 1 #consider wrap around at 23 + horus

    else:
        hours = int(hours)

    if mins == '*':
        mins = time_mins if hours == time_hours else 0
    else: 
        mins = int(mins)

    event_time = start_time.replace(hour=hours, minute=mins)
    
    if event_time < start_time:
        event_time = event_time + datetime.timedelta(days = 1)

    if event_time.date() == start_time.date():
        event_day = "today"
    else:
        event_day = "tomorrow"

    print "{0:%H}:{0:%M} {1} - {2}".format(event_time, event_day, program)



# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Simulate an alien invasion')
#     parser.add_argument(
#         '-number', type=int, help='Number of alien invaders', default=20)
#     parser.add_argument(
#         "--input", help="Input file listing cities and their roads",
#         default="world_map_small.txt")
#     parser.add_argument(
#         "--output", help="Output file for remaining cities post-invasion",
#         default="world_map_small_post_invasion.txt")
#     args = parser.parse_args()
#     main(args)
