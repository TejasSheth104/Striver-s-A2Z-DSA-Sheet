def countDigits(n: int) -> int:
    count=0
    for i in str(n):
        try:
            if (i!=0 and n%int(i)==0):
                count+=1
        except:
            continue
    return count