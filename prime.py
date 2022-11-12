from operator import length_hint
Number = int(input("Enter Number:"))
def prime(N):
    if N <= 1:
        return False
    for i in range(2, N):
        if (N % i == 0):
            return False #Not a prime number.
        return True #Prime number.
i = 2
lst = []
while True:
    if (prime(i)):
        lst.append(i)
        if (length_hint(lst) == Number):
            break
    i += 1
print("First " + str(Number) + " prime numbers are:")
print(lst)

from operator import length_hint #operator.length_hint method is utilised to find the length of an iterable such as list, tuple etc.
Number = int(input("Enter Number:")) #Required number: we want to show a sequence of prime number.
def prime(N): #define prime as a function where N is a variable.
    if N <= 1: #if true, it is not a prime number.
        return False #calling function (returning value to function).
    for i in range(2, N): #Checking the number is even or not, where 2 is the starting value in range and N can be N-1 as range will not take the last value of input N.
        if (N % i == 0): #Checking if the number is divisible or not.
            return False #Not a prime number.
    return True #Prime number.
i = 2 #First prime number is 2.
lst = [] #Creating empty list.
while True: #the loop condition is true.
    if (prime(i)): #First prime number is true.
        lst.append(i) #Adding i to the end of list.
        if (length_hint(lst) == Number): #length_hint()function:total number of elements in the list.
            break #Stop the conditions.
    i += 1 #increment i if it is prime number.
print("First " + str(Number) + " prime numbers are:") #Showing the comment line.
print(lst) #Printing the list of prime numbers.

