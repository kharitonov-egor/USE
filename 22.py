for i in range(1,100):
    x=i

    a = 3 * x + 67
    b = 3 * x - 61
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    if a==64:
        print(x)
