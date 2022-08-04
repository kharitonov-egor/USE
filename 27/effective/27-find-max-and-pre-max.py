#задача: дано число n, затем n чисел найти
#максимальное число и предмаксимальное число

n=int(input())
m=0
pm=0
for i in range(n):
    x=int(input())
    if x>m:
        pm=m
        m=x
    elif x>pm:
        pm=x

print(m,pm)