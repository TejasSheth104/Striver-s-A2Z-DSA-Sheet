def isPalindrome(string: str) -> bool:
    if string == rev_str(string, len(string)):
        return True
    else: 
        return False

def rev_str(string, n):
    if n==1:
        return string[n-1]
    return string[n-1]+ rev_str(string, n-1)
