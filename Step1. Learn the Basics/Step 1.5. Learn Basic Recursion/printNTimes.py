from  typing import *

def printNtimes(n: int) -> None:
    if (n==0): return ''
    else:
        print('Coding Ninjas', end=" ")
        printNtimes(n-1)
