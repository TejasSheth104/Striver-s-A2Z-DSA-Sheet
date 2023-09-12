## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
digits = input()
evenS=0
oddS=0
for digit in digits:
    if (int(digit)%2==0):
        evenS += int(digit)
    else:
        oddS += int(digit)
print(evenS, oddS)