import sys
from functools import reduce


def reducer_func(el_prev, el):
    return el_prev if el_prev < el else el


print(reduce(reducer_func, list(sys.stdin)))