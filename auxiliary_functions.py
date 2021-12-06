import time
from random import randint


def list_generator(a, b):
    lst = {j * randint(1, 5) for j in range(a, b)}
    print("compiled list: ", [*lst])
    return [*lst]


def result_visualiser(variant_of_sorting, data, lambda_function):
    timer = Timer()
    if len(lambda_function) > 0:
        for (dat, fnc) in list(zip(data, lambda_function)):
            # spent_time = time_measure(variant_of_sorting, dat, fnc)
            print("function: " + variant_of_sorting.__name__.upper())
            spent_time = timer.measuring(variant_of_sorting, dat, fnc)
            print("function result : ", spent_time)
            print("-" * 100)
    else:
        for dat in data:
            print("function: " + variant_of_sorting.__name__.upper())
            spent_time = timer.measuring(variant_of_sorting, dat, None)
            print("function result : ", spent_time)
            print("-" * 100)
    print("_" * 100)


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")
        self._start_time = time.perf_counter()

    def stop(self):

        """Stop the timer, and report the elapsed time"""

        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time} seconds")

    def measuring(self, testing_object, dat, fnc):
        self.start()
        res = testing_object(dat, fnc)
        self.stop()
        return res

