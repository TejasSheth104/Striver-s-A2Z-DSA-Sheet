from typing import List

def generateFibonacciNumbers(n: int) -> List[int]: 
    # Write your code here
    if n<=0: return []
    elif n==1: return [0]
    elif n==2: return [0,1]
    else:
        fibSeries = generateFibonacciNumbers(n-1)
        nextfibN = fibSeries[-1]+ fibSeries[-2]
        fibSeries.append(nextfibN)
        return fibSeries
