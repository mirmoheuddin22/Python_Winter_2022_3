import os
#my_file = r"D:\Data set for analysis!\My_matrix.csv"
#my_file = "D:\Data set for analysis!\My_matrix.csv"
my_file = r'my_matrix.csv'

print(f'Current working directory: {os.getcwd()}')
print(f'Full path of my python script: {__file__}')
#print(f'Trying to read {os.path.abspath(my_file)}')
print(f'Python project folder: {os.path.dirname(__file__)}')

my_file = os.path.join(os.path.dirname(__file__), my_file)
print(f'Trying to read {os.path.abspath(my_file)}')
m = []
with open(my_file, 'r') as f:
    i = 0
    while line:=f.readline():
        r = []
        i += 1
        print(f'{i}: {line}', end='')
        for c in line.split(';'):
            #print(c)
            r.append(c)
            #print(type(c))
        m.append(r)

#print(m)
#print(type(m[0][1]))