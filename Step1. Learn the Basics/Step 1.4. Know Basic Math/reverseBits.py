def reverseBits(num):
    # Write your code here.
    binStr=format(num,'032b')
    revBinStr=str(binStr)[::-1]
    decStr=int(revBinStr, 2)
    return decStr
