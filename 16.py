def F(n):
    if n==0:
        return 2
    elif n==1:
        return 3
    elif n>1:
        return F(n-2) * F(n-1) +n

print(F(5))