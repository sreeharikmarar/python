# simulate a dictionary using  a list

#add key "k" with value "v" to dictionary "d"


def add(a, k, v):
  b=[k,v]
  if len(a) ==0:
    a.append(b)
    return a
  for i in a:
    if i[0] == b[0]:
      c=a.index(i)
      a.remove(i)
      a.insert(c,b)

    elif not b in a:
      a.append(b)

  return a  

#return value corresponding to key "k"
#return None if key k is not present

def get(d, k):
  for i in d :
    if i[0] == k :
      return i[1]
    
  return None



    

assert(add([], "hello", 10) ==[["hello", 10]])

assert(add([["hello", 10]], "world", 20) == [["hello", 10], ["world", 20]])

assert(add([["hello",10],["world",20]], "hello", 30) == [["hello",30],["world",20]])

assert(get([["hello",10],["world",20]], "world") == 20)

assert(get([["abc",1],["def",2]], "ijk") == None)

