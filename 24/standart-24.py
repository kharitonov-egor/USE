f= open('24_1.txt')
s= f.readline()
k=0
max=0

for i in range(len(s)):
    if s[i]=='C':
        k+=1
    else:
        if k>max:
            max=k
        k=0
print(k)
        
