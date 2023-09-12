from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

def fib(element, fn1, fn2, fib_series):
    fn = fn1+fn2
    fn1 = fn2
    fn2 = fn
    fib_series.append(fn)
    if (len(fib_series) <= element):
        fib(element, fn1, fn2, fib_series)
    else: 
        print(fib_series[element-1])

element = int(input())
fn1=fn2=1
fib_series = [fn1, fn2]
fib(element, fn1, fn2, fib_series)
