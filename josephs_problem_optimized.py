"""
Joseph's Problem Algorithm
There are people standing in a circle waiting to be executed.
The counting out begins at some point in the circle and proceeds
around the circle in a fixed direction. In each step,
a certain number of people are skipped and the next person is executed.
The elimination proceeds around the circle (which is becoming smaller
and smaller as the executed people are removed),
until only the last person remains, who is given freedom.

Copied  from http://blog.dhananjaynene.com/2008/07/\
performance-comparison-c-java-python-ruby-jython-jruby-groovy/
Done simple Optimization
"""

import time
#import cProfile


class Person(object):
    __slots__ = ['count', 'prev', 'next']

    def __init__(self, count):
        self.count = count
        self.prev = None
        self.next = None

    def shout(self, shout, deadif):
        if (shout < deadif):
            return (shout + 1)
        self.prev.next = self.next
        self.next.prev = self.prev
        return 1


class Chain(object):
    __slots__ = ['first']

    def __init__(self, size):
        self.first = None
        last = None
        for current in map(Person, xrange(size)):
            #current = Person(i)
            if not self.first:
                #if self.first == None:
                self.first = current
            if last:
                ##if last != None:
                last.next = current
                current.prev = last
            last = current
        self.first.prev = last
        last.next = self.first

    def kill(self, nth):
        current = self.first
        shout = 1
        while current.next is not current:
            shout = current.shout(shout, nth)
            current = current.next
        self.first = current
        return current

if __name__ == "__main__":
    def start():
        ITER = 100000
        start = time.time()
        for i in xrange(ITER):
            chain = Chain(40)
            chain.kill(3)
        end = time.time()
        print (
            'Time per iteration = %s microseconds '
            % (end - start) * 1000000 / ITER)
    #cProfile.run('start()')
    start()
