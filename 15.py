#15

p= [i/10 for i in range(20, 100+1)]
q= [i/10 for i in range(6, 140+1)]

def f(x,a):
    return ((x in a) <= (x in p)) or (x in q)

a = set()

for x in range(i/10 for i in range(1, 1000)):
    if not f(x,a):
        a.remove(x)

print(sorted(a))
