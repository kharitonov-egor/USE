n=int(input())

summa=0

for i in range(n):
    x,y = [int(s) for s in input().split()]
    summa+=max(x,y)

if summa%2==0:
    print(summa)
else:
    print('ne povezlo')


print('everything is bad')