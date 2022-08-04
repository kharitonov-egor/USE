x= 4**2020 + 2**2017 - 15

# поиск единиц (finding ones)
count=0
while x>0:
    if x%2==1:
        count+=1
    x=x//2
print(count)