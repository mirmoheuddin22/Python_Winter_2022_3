#  * * * * * *
#   * * * * *
#    * * * *
#     * * *
#      * *
#       *
n = 90
#999 limitation of recursion.
#How many bowls do we have altogether given number of rows(n)

def sum_bowls_loop(n):
  sum = 0
  for i in range(1, n+1):
    sum += i
  return sum
print('Sum bowls using for loop for n={}: {}'.format(n, sum_bowls_loop(n)))

def sum_bowls_recursive(n):
  if n == 1:
      return 1
  else:
      s = n + sum_bowls_recursive(n-1)
      return s
#print(sum_bowls_recursive(n))
print('Sum bowls using recursion for n={}: {}'.format(n, sum_bowls_recursive(n)))

def sum_bowls_seq(n):
  return int(n * (n + 1) / 2)
print('Sum bowls using sequence for n={}: {}'.format(n, sum_bowls_seq(n)))

def sum_bowls_loop_while(rows):
  i = 1
  bowls = 0
  while i < rows:
    bowls += i
    i += 1
    if i == rows:
      bowls += i
      return bowls
print('Sum bowls using while loop for n={}: {}'.format(n, sum_bowls_loop_while(n)))
# calling bowls performance file.
if __name__ == '__main__':
    n = 998
    print('Sum bowls using for loop for n={}: {}'.format(n, sum_bowls_loop(n)))
    print('Sum bowls using while loop for n={}: {}'.format(n, sum_bowls_loop_while(n)))
    print('Sum bowls using recursion for n={}: {}'.format(n, sum_bowls_recursive(n)))
    print('Sum bowls using sequence for n={}: {}'.format(n, sum_bowls_seq(n)))

from time import time
def time_func(func, n):
    t0 = time()
    print(f'Function called: {func}')
    print(f'Result: {func(n)}')
    t1 = time()
    elapsed = round((t1 - t0)*1000, 10)
    print(f'Took {elapsed}ms')

n = 10000000
time_func(sum_bowls_loop, n)
time_func(sum_bowls_loop_while, n)
#time_func(sum_bowls_recursive, n)
time_func(sum_bowls_seq, n)