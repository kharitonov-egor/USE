#задача: дано число n, затем n чисел, найти
#максимальные 20 чисел

n=int(input())
a=[0]*20 #создаём массив в 20-ую нулями

for i in range(n):
    x = int(input())
    if x>a[0]: #если x больше самого маленького элемента в массиве, то теперь x - самый маленький
        a[0]=x
    a.sort() #сортируем массив a, так чтобы a[0] было всегда наименьшее число в массиве
print(a)