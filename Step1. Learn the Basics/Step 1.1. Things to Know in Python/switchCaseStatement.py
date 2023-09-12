from typing import *
import math

def areaSwitchCase(ch: int, a: List[float]):
    # Write your code here
    if (ch==1):
        return "{:.5f}".format(math.pi*a[0]*a[0])
    else:
        return "{:.5f}".format(a[0]*a[1], 5)
