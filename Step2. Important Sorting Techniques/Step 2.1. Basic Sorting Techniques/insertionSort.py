from typing import List

def insertionSort(a: List[int], n: int) -> None:
   for i in range(0, n):
      j=i
      while(j>0 and a[j-1]>a[j]):
         a[j-1], a[j] = a[j], a[j-1]
         j-=1
   return a      