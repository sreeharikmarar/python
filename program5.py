

# flatten a list

def flatten(a):
  flaplist=a
  list1=[]
  for sublist in flaplist:
    if isinstance(sublist,list):
      list2=flatten(sublist)
      list1.extend(list2)
    else:
      list1.append(sublist)
  return list1
  
   # pass


assert(flatten([[1,[2,3]]]) == [1,2,3])

assert(flatten([[[1,2]]]) == [1, 2])

assert(flatten([[[]]]) == [])

assert(flatten([1, [2, [3, [4]]]]) == [1,2,3,4])

