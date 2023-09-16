from typing import List

def printNos(x: int) -> List[int]: 
    # Write your code here
    if x==0: return []
    else:
        result = printNos(x-1)
        result.append(x)
        return result