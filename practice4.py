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

def greatest(n1,n2,n3):
    if (n1>n2):
        if(n1>n3):
            return n1
        else:
            return n3
    else: 
        if (n2>n3):
            return n2
        else:
            return n3

n1=int(input("Enter a number " ))
n2=int(input("Enter a number "))          
n3=int(input("Enter a number "))          
print(greatest(n1,n2,n3))






