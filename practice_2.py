n=-10
a=-1
if (n > 5):
    n=50
    if ( n > 6):
        print(n)
    
    if (n > 7):
        if(n>9):
            print("Rohab")
else :
    print(n)
# n=3
# def getN1(): #Difference between print and return
#     print("Rohab")

# def getN():
#     return "Rohab" 

# a = getN()
# # a=getN1()
# print(a)


        
###############################################################################

# type of arguments in a function 
def multiply(*numbers): # for tuples to be a part of function's argument
    total=1
    for number in numbers:
        # total = total*i
        total *= number
    return total
print(multiply(2,3,4,5,6,7,8,9))


# def saveUser(**user): # for dictionary to be a part of arguments 
#     print(user)
# saveUser(Rollno= 4492, Name="Rohab", age=23)

# def saveUser(**user): 
#     print(user["Name"])
#     print(user["Rollno"])
#     print(user["age"])





# saveUser(Rollno= 4492, Name="Rohab", age=23)


