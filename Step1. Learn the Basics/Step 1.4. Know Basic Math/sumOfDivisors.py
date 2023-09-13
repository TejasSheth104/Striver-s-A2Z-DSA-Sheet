def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    sumD=0
    for i in range(1, n+1):
        sumD += (n//i)*i
    return sumD