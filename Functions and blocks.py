j = 50
def sum(a=10, b=30):
    print(f'j={j}')
    return a + b
a = 2
b = 1
print(f'sum(a,b)={sum()}')
print(f'sum(a,b)={sum(a, b)}')

print('------------')
def sum(a=20, b=10):
    return a + b
c = 5
d = 8
print(f'sum(c,d)={sum(c, d)}')
print(f'sum(c,b)={sum(c)}')
print(f'sum(a,b)={sum()}')
print(f'sum(a,b=d)={sum(b=d)}')
print(f'sum(c=a,b=d)={sum(a=c, b=d)}')