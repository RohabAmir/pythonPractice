# n=-10
# a=-1
# if (n > 5):
#     n=50
#     if ( n > 6):
#         print(n)
    
#     if (n > 7):
#         if(n>9):
#             print("Rohab")
# else :
#     n=-60
#     print(n)
# n=3
# def getN1(): #Difference between print and return
#     print("Rohab")

# def getN():
#     return "Rohab" 

# a = getN()
# # a=getN1()
# print(a)

# function to print a pattern


# n=4
# def getN():
#     return n

# for i in range(getN()):
#     print('*' * (getN()-i))
        
###############################################################################

# type of arguments in a function 
# def multiply(*numbers): # for tuples to be a part of function's argument
#     total=1
#     for number in numbers:
#         # total = total*i
#         total *= number
#     return total
# print(multiply(2,3,4,5,6,7,8,9))


def saveUser(**user): # for dictionary to be a part of arguments 
    print(user)
saveUser(Rollno= 4492, Name="Rohab", age=23)

def saveUser(**user): 
    print(user["Name"])
    print(user["Rollno"])



saveUser(Rollno= 4492, Name="Rohab", age=23)



