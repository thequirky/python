Apply decorator with `@profile` to a function to profile and print report.  
Provided by Sebastiaan Mathôt.


```python
import cProfile, pstats, io


def profile(fnc):
    """A decorator that uses cProfile to profile a function and print report"""
    
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval
        
    return inner
    ```
