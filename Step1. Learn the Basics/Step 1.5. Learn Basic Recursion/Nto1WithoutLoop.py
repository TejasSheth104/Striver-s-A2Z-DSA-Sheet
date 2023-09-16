from typing import List

revLs = list()
def printNos(x: int) -> List[int]: 
    # Write your code here 
    if x==0: return []
    else:
        revLs.append(x)
        printNos(x-1)
    return revLs
