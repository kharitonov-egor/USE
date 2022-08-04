# задача: дано число n, затем n пар чисел, в каждой строке по одной паре
# выбрать из каждой пары по одному числу так, чтобы сумма всех выбранных
# чисел была максимальна и делилась на 3
# СУЩЕСТВОВАНИЕ ОТВЕТА ГАРАНТИРУЕТСЯ ВЫСШИМИ СИЛАМИ ВСЕЛЕННОЙ

n = int(input())
summa = 0
md1 = 1000000000
pmd1 = 1000000000
md2 = 1000000000
pmd2 = 1000000000
for i in range(n):
    x, y = [int(s) for s in input().split()]
    if (y > x):
        x, y = y, x
    summa += x
    diff = x - y
    if (diff % 3 ==1):
        pmd1 = min(pmd1,diff)
        md1,pmd1 = min(md1,pmd1),max(md1,pmd1)
    if(diff % 3 ==2):
        pmd2 = min(pmd2,diff)
        md2,pmd2 = min(md2,pmd2),max(md2,pmd2)
if (summa % 3 == 0):
    print(summa)
else:
    if(summa % 3 == 1):
        if(md2+pmd2 < md1):
            print(summa - md2 - pmd2)
        else:
            print(summa - md1)
    elif(summa %3 == 2):
        if(md1 + pmd1 < md2):
            print(summa-md1-pmd1)
        else:
            print(summa - md2)
