
# Merge two sorted (ascending) lists. Return the merged list. The "merged"
# list is also sorted.

def merge(a, b):
  c = []
  while len(a) and len(b):
    if a[0]<b[0]:
      c.append(a.pop(0))
    else:
      c.append(b.pop(0))
  c.extend(a)
  c.extend(b)
  return c 
  
   # pass


assert(merge([1], [2]) == [1,2])

assert(merge([10, 20], [30]) == [10, 20, 30])

assert(merge([10, 30, 40], [32, 33, 45, 57]) == [10,30,32,33,40,45,57])

assert(merge([20, 25, 27, 34], [1, 10, 23]) == [1,10,20,23,25,27,34])

assert(merge([1], []) == [1])

assert(merge([], [1, 2]) == [1,2])

