n=int(input())  
# taking n as a input 
## write your code !!
ans = 0
backup = n
while n>0:
    rem = n%10
    n = n//10
    ans = ans*10 + rem

if (ans == backup):
    print('true')
else:
    print('false')
