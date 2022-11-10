l1 = [14231, 2523, 252, 7578, 967]
print(l1)
print(l1[2])
print(l1[1:4])
l1.append(4754)
print(l1)
l1.insert(2, 4235634)
print(l1)
l1.remove(252)
print(l1)
l1.pop(4)
print(l1)

for i in range(len(l1)):
    print(f'el {i}={l1[i]}')

print('-------')

for var in l1:  #var/val as a variable (or value).
    print(f'var={var}')

l2 = l1
print(f'l2={l2}')
l3 = l1.copy()
print(f'l3={l3}')
print('-------')
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
print(f'l1={l1}')
print(f'l2={l2}')
print(f'l3={l3}')

