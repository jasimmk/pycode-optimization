#!/usr/bin/python
"""
Return a List of Duplicate items in a Super list
"""
import time
import functools


def timed(func):
    """
    Wrapper for Functions to print Time Consumed by each function
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        ITER = 100
        start = time.time()
        for x in xrange(ITER):
            result = func(*args, **kwargs)

        print "Elapsed Time for %s: %s microseconds"\
            % (func.__name__, (time.time() - start) * 1000000 / ITER)
        return result
    return wrapped


def list_count_set(huge_list):
    return list(set([x for x in huge_list if huge_list.count(x) > 1]))


def list_multi_list_compare(huge_list):
    non_dup_list = []
    dup_list = []
    for x in huge_list:
        if x in non_dup_list:
            dup_list.append(x)
        else:
            non_dup_list.append(x)
    return dup_list


def list_multi_list_compare_opt(huge_list):
    non_dup_list = []
    dup_list = []

    for x in tuple(huge_list):
        if x in non_dup_list:
            dup_list.append(x)
        else:
            non_dup_list.append(x)
    return dup_list

if __name__ == "__main__":
    def main_func():
        #l = [x for x in range(10000)]
        #l += [x for x in range(1, 100, 3)]
        #l += [x for x in range(100, 2000, 5)]

        l = [x for x in range(0, 10000)] + [x for x in range(0, 200, 3)]
        print "length of list: %s" % (len(l))
        timed(list_multi_list_compare_opt)(l)
        timed(list_count_set)(l)
        timed(list_multi_list_compare)(l)

    main_func()
