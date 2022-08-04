# дано число n, затем n пар чисел
# найти максимальную чётную сумму, если
# можно выбрать из каждой пары
# ровно по одному числу

# как считать пару чисел в одной строке в питоне?
n = int(input())
s = 0
md = 100000000000000
for i in range(n):
    x, y = [int(k) for k in input().split()]
    s += max(x,y)
    #ой блин, а что если надо было на этом шаге в сумму
    #прибавить не max(x,y), а min(x,y) ?    ну, сами понимаете,
    #для чётности. Исправим эту ошибку
    diff = max(x,y) - min(x,y)

    if(diff % 2 != 0):
        if(diff < md):
            md = diff
#в какой-то паре, вероятно, придётся взять не max(x,y),
# а min(x,y), пожертвовав при этом частью суммы, но получив
# чётность. Чтобы замена max(x,y) ---> min(x,y) поменяла
# чётность суммы, надо чтобы max(x,y)-min(x,y) % 2 != 0
if(s%2==0):
    print(s)
else:
    if(md == 100000000000000):
        print('The answer does not exist')
    else:
        print(s - md)