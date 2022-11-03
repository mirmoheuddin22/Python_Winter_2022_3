s1 = 'sfhkjdfsjnsfk'
print(s1[2])
print(s1[2:6])
print(s1[2:])
print(s1[:2])
print(s1[-2:])
s2 = s1[:2] + s1[-2:]
print(s2)

print(s1.find('fs'))
s3a = '23453444;23444433;24553435;245355'
s3b = "24234355;23554555;55325355;352535"
s4 = "I can't"
s5 = 'He said "my name is....."'
s6 = 'He said "I can\'t"'

print(s3a.split(';'))
print(s3b.split(';')[1])

s5 = 'He said "my name is....."'
s6 = 'He said "I can\'t"'
s6 = "He said \"I can't\""
s6 = "He \\nsaid \"I \tcan't\""
print(s5)
print(s6)

print(ord('a'))
print(ord('b'))
print(chr(65), end='')
print(chr(32), end='')
print(chr(66), end='')


