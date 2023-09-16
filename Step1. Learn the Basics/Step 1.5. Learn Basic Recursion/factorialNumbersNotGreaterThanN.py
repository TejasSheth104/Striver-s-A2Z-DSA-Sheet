from typing import *

def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)

def factorialNumbers(n: int, curr=1) -> List[int]:
    # Write your code here
    if fact(curr)<=n:
        return [fact(curr)]+factorialNumbers(n,curr+1)
    else:
        return []
    return ls
