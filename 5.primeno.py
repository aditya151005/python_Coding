# check the prime no
# n=int(input("Enter a number"))
# if n<2:
#     print(f"n is not a prime Number")
# else:
#     for i in range(2,n):
#         if n%2==0:
#             print(f"{n} is not a prime No")
#             break
#     else:
#         print(f"{n} is a prime Number")
# # prime no between two numbers
# n1=int(input("Enter the first number"))
# n2=int(input("Enter the second number"))
# for i in range(n1,n2,1):
#     for j in range(2,i):
#          if i%j==0:
#              break
#     else:
#         print(i)
#first n prime numbers
n=int(input("Enter a number"))
count=0
number=2
while count<n:
    for i in range(2,number):
        if number%i==0:
            break
    else:
        print(number)
        count=count+1
    number=number+1
        