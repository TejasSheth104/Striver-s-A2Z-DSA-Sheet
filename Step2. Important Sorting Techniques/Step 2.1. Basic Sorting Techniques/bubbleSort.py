from typing import List

def bubbleSort(arr: List[int], n: int):
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# time complexity
#  Worst = Average = O(n*n)
#  series of n natural nos (n-1, n-2, n-3,.....,3,2 [1])
#  = (n*n+1)/2

# Best = O(n)
# break out after 1st loop, if no swaps are done.

# optimised
from typing import List

def bubbleSort(arr: List[int], n: int):
    for i in range(n-1, 0, -1):
        ifSwap=0
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                ifSwap=1
        if ifSwap==0: break
    return arr