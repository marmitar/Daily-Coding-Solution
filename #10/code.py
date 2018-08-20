from scheduler import Scheduler
from time import sleep

sched = Scheduler()

sched.runAfter(200, print, "Foo")
sched.runAfter(100, print, "Bar", "Baz", end=' ')
sched.runNow(print, "Foo", end=' ')

sleep(.3)  # wait for the threads to finish
sched.stop()
