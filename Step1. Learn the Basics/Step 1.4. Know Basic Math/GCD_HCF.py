def calcGDC(n:int, m: int) -> int:
    if m==0:
        return n
    else:
        return calcGDC(m, n%m)