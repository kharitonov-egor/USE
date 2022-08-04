n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))

maxim=0
for i in range(n):
    for j in range(i+1,n):
        if((a[i]*a[j])%14 == 0):
            if (a[i]*a[j] > maxim):
                maxim = a[i]*a[j]

print(maxim)
