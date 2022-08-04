from functools import lru_cache

def moves(h):
    return h+1, h*2

@lru_cache(None)
def f(h):
    if 50<=h<=70:
        return 'СР'
    elif h>70:
        return 'П1'
    elif any(f(m) == 'СР' for m in moves(h)):
        return 'П1'
    elif any(f(m)=='П1' for m in moves(h)):
        return 'В1'
    elif any(f(m)=='В1' for m in moves(h)):
        return 'П2'
    elif all(f(m)=='П1' or f(m) == 'П2' for m in moves(h)):
        return 'В2'

for i in range(1,80):
    print(i,':',f(i))