from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.


def is_prime(n):
    if n <= 1:
        return 'NO'
    elif n <= 3:
        return 'YES'
    elif n % 2 == 0 or n % 3 == 0:
        return 'NO'
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return 'NO'
        i += 6
    
    return 'YES'

num = int(input())
print(is_prime(num))
