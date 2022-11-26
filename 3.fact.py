# n=int(input("Enter a number"))
# if n<0:
#     print("Factorial not possible")
# else:
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     print(f"factorial of a number {n} is {f}") #5040(7)
# using function
# def fact(n):
#     if n<0:
#        print("Factorial not possible")
#     else:
#        f=1
#        for i in range(1,n+1):
#          f*=i
#        return f
# n=int(input("Enter a number"))
# f=fact(n)
# print(f"factorial of a number {n} is {f}") #120 (5)
# using recursion functions(fn calling itself is called recursive fn )
#Recursion(1.Base case(stopping condition) 2. recursive case)
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("Enter a number"))
# f=fact(n)
# print(f"factorial of {n} is {f}")#Enter a number4
# # factorial of 4 is 24