def algarv(x):
    i=2
    while i<x:
        if x%i==0:
            return False
        i=i+1
    return True


n=1
while n<100:
    if algarv(n):
        print(n)
    n=n+1