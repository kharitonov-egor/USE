x=125+25**3+5**9

#https://inf-ege.sdamgia.ru/problem?id=13362
#поиск 0 (finding 0)

counter=0
while (x>0):
    if (x%5==0):
        counter+=1
    x=x//5

print(counter)