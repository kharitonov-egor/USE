#+1,*2,+5

def f(curr,end):
    if curr>end or curr==10:
        return 0
    if curr==end:
        return 1

    return f(curr+1,end) + f(curr*2,end) + f(curr+5,end)

print(f(1,8)*f(8,16))

#https://inf-ege.sdamgia.ru/problem?id=17340