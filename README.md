Next Cron Task 
===
Calculates the next times the specified cron jobs will fire.

Reads the cron jobs from stdin in the following format 
    `30 1 /bin/run_me_daily`

You can specify the start time to calculate from with a positional argument in format `HH:MM`

Usage
---

Pipe the cron config file into next_task.py followed by a positional argument specifying the time (optional, defaults to now)

        cat config.cron | python next_task.py 14:45


Background
---

The scheduler config looks like this:

    30 1 /bin/run_me_daily
    45 * /bin/run_me_hourly
    * * /bin/run_me_every_minute
    * 19 /bin/run_me_sixty_times

The first field is the minutes past the hour, the second field is the hour of the day and the third is the command to run. For both cases * means that it should run for all values of that field. In the above example run_me_daily has been set to run at 1:30am every day and run_me_hourly at 45 minutes past the hour every hour. The fields are whitespace separated and each entry is on a separate line.

This program, when fed this config to stdin and the current time in the format HH:MM as command line argument outputs the soonest time at which each of the commands will fire and whether it is today or tomorrow. When it should fire at the current time that is the time you should output, not the next one.

For example given the above examples as input and the command-line argument 16:10 the output should be

    1:30 tomorrow - /bin/run_me_daily
    16:45 today - /bin/run_me_hourly
    16:10 today - /bin/run_me_every_minute
    19:00 today - /bin/run_me_sixty_times

We will want to run your tool, so please supply instructions for running it. Additionally, it must work on at least one of OSX and Linux (so we can run it on our dev boxes), ideally both.

Please submit all code as attachments, not in the body of the email, as formatting is often lost or mangled. If you want to attach multiple files please do so as an archive (e.g. zip, tar, git bundle, etc).