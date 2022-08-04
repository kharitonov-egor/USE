x=36**7 + 6**19 -18
counter=0
while x>0:
    if x%6==5:
        counter+=1
    x=x//6
print(counter)