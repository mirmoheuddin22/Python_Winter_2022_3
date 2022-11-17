d1 = {'Jan': 'January', 'Feb':'February', 'Mar': 'March'}
print(d1)
print(d1['Feb'])
d2= {'Jan': 'January', 'Feb':'February', 'Mar': 'March','Feb':'Febror'}
print(d2)
for k in d2.keys():
     print(f'{k}: {d2[k]}')

print('---------')
for k, v in d2.items():
       print(f'{k}:{v}')
print('---------')
for v in d2.values():
     print(v)
My_team = dict([ ('Colorado', 'Rockies'), ('Boston', 'Red Sox'), ('Minnesota', 'Twins'), ('Milwaukee', 'Brewers'), ('Seattle', 'Mariners')])
print(My_team)
My_team = dict( Colorado='Rockies', Boston='Red Sox', Minnesota='Twins', Milwaukee='Brewers', Seattle='Mariners' )
print(My_team)
print(type(My_team))
print(My_team['Minnesota'])
#Adding an entry to an existing dictionary:
My_team['Kansas City'] = 'Royals'
print(My_team)
#To delete an entry:
del My_team['Seattle']
print(My_team)
d = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
print(d[0])
d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}
print((1, 1))
d = {0: 'a', 1: 'a', 2: 'a', 3: 'a'}
print(d[0] == d[1] == d[2])
print('Milwaukee' in My_team)
print(len(My_team))
d = {'a': 10, 'b': 20, 'c': 30}
print(d.clear())
d = {'a': 10, 'b': 20, 'c': 30}
print(d.get('b'))
d = {'a': 10, 'b': 20, 'c': 30}
print(list(d.items()))
print(list(d.items())[1][0])
print(list(d.items())[1][1])
print(list(d.keys()))
print(list(d.values()))
print(d.pop('b'))
print(d.pop('z', -1))
print(d.popitem())
