from os import *
from sys import *
from collections import *
from math import *

sum = 0
num = str(input())
l = len(num)
for n in num:
    sum += int(n)**int(l)
print("true") if (sum == int(num)) else print("false")
