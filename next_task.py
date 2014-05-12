#!/usr/bin python

# Date 2014-05-12
# Author Jordan Burgess

""" Calculates the next times the specified cron jobs will fire.

    Reads the cron jobs from stdin in the following format
        `30 1 /bin/run_me_daily`

    You can specify the start time to calculate from with a positional
    argument in format (defaults to now)
        `HH:MM`

    eg.
        `cat config.cron | python next_task.py 14:45`
 """

import argparse
import sys
import datetime

def next_cron_events(args):
    """ Returns the next time cron jobs will execute.
    """
    start_time = datetime.datetime.now()

    if args.time:
        start_hour, start_minute = args.time.split(':')
        start_time = start_time.replace(hour=int(start_hour), minute=int(start_minute))

    for line in sys.stdin:

        day_offset = 0
        cron_minute, cron_hour, program = line.strip().split(' ')

        if cron_minute == '*':
            if cron_hour == '*' or int(cron_hour) == start_time.hour:
                next_event_minute = start_time.minute
            else:
                next_event_minute = 0
        else:
            next_event_minute = int(cron_minute)


        if cron_hour == '*':
            if next_event_minute >= start_time.minute:
                next_event_hour = start_time.hour
            else:
                day_offset, next_event_hour = divmod(start_time.hour + 1, 24)
        else:
            next_event_hour = int(cron_hour)
            if next_event_hour < start_time.hour:
                day_offset += 1
        
        next_event = start_time.replace(
            day=start_time.day + day_offset,
            hour=next_event_hour,
            minute=next_event_minute)

        event_day = "tomorrow" if day_offset else "today"

        print("{0:%H}:{0:%M} {1} - {2}".format(next_event, event_day, program))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate the next time a cron job will execute')
    parser.add_argument('time', nargs='?', help="HH:MM - Time from which to calculate next cron")
    args = parser.parse_args()
    next_cron_events(args)
