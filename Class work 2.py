#Sum all rows in l1 as a list of values:
l1 = [[5, 7, 8],[3, 5, 6],[4, 2, 1]]
lst1 = []
for row in l1:
      if (sum(row)):
            lst1.append(sum(row))
print('Sum of all rows in l1:',lst1)
#Sum all columns in l1 as a list of values:
list1 = [5, 7, 8]
list2 = [3, 5, 6]
list3 = [4, 2, 1]
zipped = zip(list1,list2,list3) #Iterating over the columns of the sublists.
print(type(zipped))
print(zipped) #Holding an iterator object
#print(list(zipped))
lst2 = []
for col in zipped:
      if (sum(col)):
            lst2.append(sum(col))
print('Sum of all columns in l1:',lst2)
#smart way(quicker):
rows_sum = [sum(row) for row in l1]
print('Sum of all rows in l1:', rows_sum)
columns_sum = [sum(col) for col in zip(*l1)]
print('Sum of all columns in l1:',columns_sum)
#Sum all elements of l1:
list4 = lst1
total = sum(list4)
print('Sum of all elements in l1:',total)