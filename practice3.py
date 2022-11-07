# function to print a pattern


# n=4
# def getN():
#     return n

# for i in range(getN()):
#     print('*' * (getN()-i))





n=3
for i in range(0,n):
    if(i==1):
        print("*",end="")
        print(" ",end="")
        print("*")
    else:
        print("*" * n)
