from typing import *

def countFrequency(n: int, m: int, edges: List[List[int]]):
    # print(edges)
    # precompute
    hashh = [0]*n
    for i in range(n):
        if (edges[i]<=n):
            hashh[edges[i]-1] += 1
    return hashh
