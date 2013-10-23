#!/usr/bin/python
"""
Return a List of Duplicate items in a Super list
"""
import time
import functools


def timed(func):
    """Print Time for Function Execution"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print "Execution time for %s is %f" % (func.__name__, elapsed)
        return result

    return wrapper


@timed
def list_count_set(huge_list):
    return list(set([x for x in huge_list if huge_list.count(x) > 1]))


@timed
def list_multi_list_compare(huge_list):
    non_dup_list = []
    dup_list = []
    for x in huge_list:
        if x in non_dup_list:
            dup_list.append(x)
        else:
            non_dup_list.append(x)
    return dup_list


@timed
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

        l = [x for x in range(0, 100000)] + [x for x in range(0, 200, 3)]
        print "length of list: %s" % (len(l))
        list_multi_list_compare_opt(l)
        list_count_set(l)
        list_multi_list_compare(l)

    main_func()
