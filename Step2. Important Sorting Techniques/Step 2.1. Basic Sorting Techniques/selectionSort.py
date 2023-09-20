from typing import List

def selectionSort(arr: List[int]) -> None: 
    # Write your code here
    n = len(arr)
    for i in range(0, n-1):
        minValue=i
        for j in range(i, n):
            if arr[j]<arr[minValue]: minValue=j
        arr[minValue], arr[i] = arr[i], arr[minValue]
    return arr

# time complexity
#  Best = Worst = Average = O(n*n)
#  series of n natural nos (n-1, n-2, n-3,.....,3,2 [1])
#  = (n*n+1)/2