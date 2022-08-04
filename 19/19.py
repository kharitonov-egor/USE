from functools import lru_cache

def moves(h):
    return h+3, h*2

@lru_cache(None)
def f(h):
    if h>=33:
        return 'СР'
    elif any(f(m)== 'СР' for m in moves(h)):
        return 'П1'
    elif all(f(m)=='П1' for m in moves(h)):
        return 'B1'
    elif any(f(m)=='B1' for m in moves(h)):
        return 'П2'
    elif all(f(m) == 'П1' or f(m)=='П2' for m in moves(h)):
        return 'B2'

for i in range(1,40):
    print(i, f(i))
