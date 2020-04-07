import cProfile
import pstats


def profile(fnc):
    """
    A decorator that uses cProfile to profile a function and print a report
    """

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        sortby = 'cumulative'
        with open('profile_report.txt', 'a') as f:
            pstats.Stats(pr, stream=f).strip_dirs().sort_stats(sortby).print_stats()
        return retval

    return inner
