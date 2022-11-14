#def remove_words(l4, remove_words):
    #for word in list(l4):
        #if word in remove_words:
            #l4.remove(word)
            #return l4
#list1 = [14231, 2523, 252, 'Hello from Python 3', 7578, 967]
#words = ['Hello from Python 3']
#print(remove_words(list1, words))
l4 = [14231, 2523, 252, 'Hello from Python 3', 7578, 967]
print(l4)
l5 = l4[3].split()
print(l5)
l5.remove('Python')
print(l5)
l6 = ' '.join(l5)
l4.remove('Hello from Python 3')
l4.insert(3, l6)
print('Extracting the word Python:',l4)
l4.remove('Hello from 3')
print(l4)
l4.insert(3,3)
print(l4)
list1 = l4
total = sum(list1)
print('Sum of all number in l4:',total)
#Another way:
#l4.remove('Hello from Python 3')
#print(l4)
#l4.insert(3,'hello from 3')
#print('Extracting the word Python:',l4)
#l4.remove('hello from 3')
#print(l4)
#l4.insert(3,3)
#print(l4)
#list1 = l4
#total = sum(list1)
#print('Sum of all number in l4:',total)
#l5 = [x*2 for x in l4]
#print(l5)
#print('words =', l5)
#l5.remove('Python')
#print(l5)
#final_string =' '.join(l5)
#print(final_string)

