# partition a list using its first element
# return a list-of-partitioned-lists


def partition(a):
  x=[]
  y=[]
  z=[]
  i = a[0]
  for j in a:
    if j < a[0]:
      x.append(j)
    if j > a[0]:
      y.append(j)

  z = [x,y]  
 
  return z   
      
      


#    pass




assert(partition([10, 8, 2, 11, 14, 6,1, 13]) == [[8,2,6,1],[11,14,13]])

assert(partition([1,2,3,4]) == [[],[2,3,4]])

assert(partition([1]) == [[],[]])

assert(partition([4,3,2,1]) == [[3,2,1],[]])


