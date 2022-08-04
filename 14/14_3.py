x = 49**10 + 7**30 - 49

#ищем 6-ки (finding 6)
#https://inf-ege.sdamgia.ru/test?theme=247
count=0
while x>0:
    if x%7==6:
        count+=1
    x=x//7

print(count)