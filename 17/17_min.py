a=7525
b=13486
counter=0
min=20000
for i in range(a,b+1):
    if i%7==0 and i%6!=0 and i%9!=0 and i%14!=0 and i%21!=0:
        counter+=1
        if i<min:
            min=i


print(counter, min)

#https://inf-ege.sdamgia.ru/problem?id=27613