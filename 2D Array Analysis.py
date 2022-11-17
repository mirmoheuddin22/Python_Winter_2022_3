#Accessing Single Element:
Array = [[1,2,3],[4,5,6],[7,8,9]]
print("Element at [1][0]=",Array[1][0])
# Accessing an Internal Array:
print("Element at [2]=",Array[2])
#raversing Values in Python 2D Array:
Array=[[1,2,3],[4,5,6],[7,8,9]]

for _ in Array:
    for i in _:
        print(i,end=" ")
    print()
#Inserting Values in Python 2D Array:
import array
Array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Original Array")
for _ in Array:
    for i in _:
        print(i, end=" ")
    print()

Array.insert(2, [11, 12, 13])

print("Modified Array")
for _ in Array:
    for i in _:
        print(i, end=" ")
    print()
#Inserting Values in Python 2D Array:
import array
Array=[[1,2,3],[4,5,6],[7,8,9]]

print("Original Array")
for _ in Array:
    for i in _:
        print(i,end=" ")
    print()

Array[1].insert(2,12)

print("Modified Array")
for _ in Array:
    for i in _:
        print(i,end=" ")
    print()
#Updating Values in Python 2D Array:
Array=[[1,2,3],[4,5,6],[7,8,9]]

print("Original Array")
for _ in Array:
    for i in _:
        print(i,end=" ")
    print()

Array[1][2]=16

print("Modified Array")
for _ in Array:
    for i in _:
        print(i,end=" ")
    print()
#Updating an Inner Array:
Array =[[1,2,3],[4,5,6],[7,8,9]]

print("Original Array")
for _ in Array:
    for i in _:
        print(i,end=" ")
    print()
new_Array=[10,11,12]
Array[1]=new_Array

print("Modified Array")
for _ in Array:
    for i in _:
        print(i,end=" ")
    print()
#Deleting an Inner Array:
from array import *
Array=[[1,2,3],[4,5,6],[7,8,9]]

print("Original Array")
for _ in Array:
    for i in _:
        print(i,end=" ")
    print()

del(Array[1][2])

print("Modified Array")
for _ in Array:
    for i in _:
        print(i,end=" ")
    print()
#Deleting an Inner Array:
import array
Array=[[1,2,3],[4,5,6],[7,8,9]]

print("Original Array")
for _ in Array:
    for i in _:
        print(i,end=" ")
    print()

del(Array[1])

print("Modified Array")
for _ in Array:
    for i in _:
        print(i,end=" ")
    print()
