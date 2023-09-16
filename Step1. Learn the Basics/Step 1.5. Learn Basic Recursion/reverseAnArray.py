from typing import *

ls = list()
def reverseArray(n: int, nums: List[int]) -> List[int]:
    # Write your code here
    if n==0: return ls
    else:
        ls.append(nums[n-1])
        n-=1
        reverseArray(n,nums)
    return ls
