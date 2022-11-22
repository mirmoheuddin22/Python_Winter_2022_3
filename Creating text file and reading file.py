myfile = open('file.txt','w') #open a file and overwriting file based on old file.
myfile = open('file.txt','a') #open a file and and showing the next line of new content of file.
myfile = open('D:\\Python_Winter_2022_3\\file.txt','a') #putting file in any location.
myfile.write('Good student.\n Excellent student')
for i in range(20):
    myfile.write("my serial number is %d\n" % i)
    myfile.write("my serial number is %d\n" % (i+1))
myfile.close()
myfile = open('file.txt','r')
print(myfile.read(3))
print(myfile.read(9))
print(myfile.readline(3))
print(myfile.readline())
print(myfile.readline())
print(myfile.readlines())
print(myfile.readlines()[4])
for line in myfile:
    print(line)
    print(len(line))
    print(line.split(' '))
    print(len(line.split(' ')))
myfile.close()