a=2481
b=14832
counter=0
max=0
for i in range(a,b+1):
    if (i%5==0 or i%11==0) and (i%6!=0 and i%7!=0 and i%10!=0 and i%23!=0):
        counter+=1
        max=i


print(counter, max)

#https://inf-ege.sdamgia.ru/problem?id=27616