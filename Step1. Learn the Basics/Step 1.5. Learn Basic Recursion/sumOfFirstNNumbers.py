from typing import List

def sumFirstN(n: int) -> int:
    # Write your code here.
    if n==0: 
        return 0
    else:
        return n + sumFirstN(n-1)
    
# alternate 

from typing import List
def sumFirstN(n: int) -> int:
    # Write your code here.
    sum=(n*(n+1))//2
    return sum