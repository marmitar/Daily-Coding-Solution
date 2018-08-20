from threading import Thread
from dataclasses import dataclass
from time import time
from heapq import heappop, heappush


@dataclass(eq=True, order=True, frozen=True)
class ScheduledFunction:
    """Helper dataclass used for heap"""
    when: float
    function: callable
    args: tuple
    kwargs: dict


class Scheduler(Thread):
    """
    This class is a thread that arranges functions to be called at specific
    times.

    Call stop() to kill the scheduler thread.
    """

    def __init__(self):
        """
        Constructor already starts the thread. This can be modified
        with the start argument.
        """
        Thread.__init__(self)
        self.__sched__ = list()
        self.__running__ = True
        self.start()

    @staticmethod
    def __function_init__(function: ScheduledFunction):
        Thread(
            target=function.function,
            args=function.args,
            kwargs=function.kwargs
        ).start()

    def run(self):
        while self.__running__:
            if len(self.__sched__) > 0 and self.__sched__[0].when <= time():
                func = heappop(self.__sched__)
                Scheduler.__function_init__(func)

        del self

    def stop(self):
        self.__running__ = False

    def runAt(self, when, function, *args, **kwargs):
        """Set a function to run at a specific moment."""

        entry = ScheduledFunction(when, function, args, kwargs)
        heappush(self.__sched__, entry)

    def runNow(self, function, *args, **kwargs):
        """Set a function to run now."""

        func = ScheduledFunction(0, function, args, kwargs)
        Scheduler.__function_init__(func)

    def runAfter(self, wait_time, function, *args, **kwargs):
        """Set a function to run after an amount of time (in ms)."""

        when_to_run = time() + wait_time/1000
        self.runAt(when_to_run, function, *args, **kwargs)
