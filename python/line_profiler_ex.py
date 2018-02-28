# line_profiler
import line_profiler


# add @profile decorator
# no need to import anything
@profile
def slow_function(a, b, c):
    pass


# run script
# kernprof -l script_to_profile.py


# see results
# python -m line_profiler script_to_profile.py.lprof
