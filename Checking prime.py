#n = int(input("Enter Number:"))
#for i in range(2,n):
      #if (n%i) == 0:
        #print('Not prime')
        #break
#else:
 #print('prime')
from operator import length_hint
#import math
Number = int(input("Enter Number:"))
def prime(N):
    for i in range(2, N-1):
        if (N % i == 0):
            return False #Not a prime number.
    return True #prime number.
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
#import numpy as np
#import seaborn as sns
#import pandas as pd
#import matplotlib.pyplot as plt

#n = 20

#x = np.arange(n)
#y1 = np.sqrt(x)
#y2 = x
#df = pd.DataFrame({"O(√n)":y1,"O(n)":y2})
#sns.set_theme()
#sns.lineplot(data = df)
#plt.show()

#def isprime(n):
    #if n <= 1:
        #return False
    #for i in range(2, n):
        #if n % i == 0:
            #return False
    #return True
#N = int(input())
#for i in range(N + 1):
    #if isprime(i):
        #print(i)
#my_list =[1,4,67,89,34,56,2,6,7]
#prime=[]
#for i in my_list:
    #c=0
    #for j in range(1,i):
        #if i%j==0:
            #c+=1
    #if c==1:
        #prime.append(i)
#print(prime)