# n=4
# for i in range(4,-1,-1):
#     print("*" * (i))


# WITHOUT IF STATEMENT 
n=4
for i in range(4,0,-1):
    print("*" * (i))

# WITH IF STATEMENT ( for a space in the end)
n=4
for i in range(5):
    if (i!=4):
        print("*" * (n-i))
    else :
        print(' ')




for i in range(0,7):
    if(i==3):
        print()  
        continue
    print("*****",end="")
    print()       





for i in range(0,4):
    print("*" * ( i+1))

for i in range(4,0,-1):
    print("*" * i)


n=4
for i in range (4):
    print(" " * (n-i-1), end="  ")
    print("*" * (2*i+2))
for i in range (4,0,-1):
    print(" " * (n-i), end="  ")
    print("*" * (2*i))

n=4
for i in range (4):
    print(" " * (n-i-1), end="  ")
    print("*" * (2*i+2))
print()
for i in range (4,0,-1):
    print(" " * (n-i), end="  ")
    print("*" * (2*i))


n=4
for i in range (4):
    print(" " * (n-i-1), end="")
    print("*" * (i+1),end="")
    print(' ', end="")
    print("*" * (i+1))
    
print()


for i in range (4,0,-1):
    print(" " * (n-i), end="")
    print("*" * i , end="")
    print(" ", end="")
    print("*" * i )

######################################################################################################
 
# def table(num):
#     for i in range(1,11):
#         print(f"{num}X{i}={num*i}")
# num=int(input("Enter a number "))
# table(num)


# def factorial_iter(n):
#     product=1
#     for i in range(n):
#         product= product*(i+1)
#     return product
# n=int(input("Enter a number "))
# print(factorial_iter(n))

# def factorial_rec(n):
#     if (n==1 or n==0):
#         return 1
#     else:
#         return n* factorial_rec(n-1)
# n=int(input("Enter a number "))
# print(factorial_rec(n))


# def Sum_rec(n):
#     if ( n==1 or n==0): # Base condition
#         return 1
#     else:
#         return n + Sum_rec(n-1)
# s=Sum_rec(5)
# print(s)

# name= "Rohab"                           
# def getCapitalLetter():
#     return name[0] #Block of code
# name="Ahmed" #Variable Hoisting         name="Ahmed"





# name= "Rohab"
# def getCapitalLetter(): #scope of a function
#     return name[0]
# print(getCapitalLetter())
# name="Ahmed" #Variable Hoisting
# print(getCapitalLetter())

# def greatest(n1,n2,n3):
#     if (n1>n2):
#         if(n1>n3):
#             return n1
#         else:
#             return n3
#     else: 
#         if (n2>n3):
#             return n2
#         else:
#             return n3

# n1=int(input("Enter a number " ))
# n2=int(input("Enter a number "))          
# n3=int(input("Enter a number "))          
# print(greatest(n1,n2,n3))






