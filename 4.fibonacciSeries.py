n=int(input("How many fibonacii series to be displayed"))
first=0
second=1
for i in range(n):
    print(first)
    temp=first
    first=second
    second=temp+first