s=input()
n=len(s)
counter=1
maxim=0
for i in range(1,n):
    if(s[i]==s[i-1]):
        counter=counter+1
        if counter>maxim:
            maxim=counter
    else:
        counter=1
print(n)
print(maxim)
