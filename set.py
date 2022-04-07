# e={}
# print(e,type(e))#set
# v={1,2,6,"hello",("hlo",2)}
# print(v,type(v))#{('hlo'),2,"hello",1,2,6} set
# n={10,20,30}
# print(n[1])#TypeError:set object is not subscriptable
# d={1,3,5}
# print(d,type(d))#set{1,3,5}
# k=frozenset(d)
# print(k[0])#TypeErorr:set object is not subscriptable
# a={1,2,3}
# b='hello',1,2,3
# a.add(b)
# print(a)#{1,2,3,('hello',1,2,3)}set
# b={1,5,7}
# b.clear()
# print(b)#set()
# a={2,3,4}; b={3,5,6}; c={22,44,55}; d={2,5,9}
# print(a.intersection(b))#{3}
# print(a.intersection(c))#()
# print(a.intersection(d))#{2}
# print(b.intersection(d))#{5}
# a={1,2,3}
# b={4,3,5}
# c={4,3,7}
# a.update(b)#{1,2,3,4,5}
# # a.update(c)#{1,2,3,4,5,7}
# print(a)
# a={1,2,3}
# b={4,3,5}
# print(a.union(b))#{1,2,3,4,5}
# # print(b.union(a))#{1,2,3,4,5}
# a={5,10,20,25,30}
# b={10,21,5}
# print(a.difference(b))#{20,25,30}
# print(b.difference(a))#{21}
# print(a-b)#{20,25,30}
# print(b-a)#{21}
# z={55,56,57,73,45,23}
# z.discard(4)
# print(z)#{55,56,57,73,45,23}
# z.discard(73)
# # print(z)#{55,56,57,45,23}
# v={26,7,11,4,23}
# v.pop()
# print(v)#{26,7,11,23}
# a={1,2,3}
# b={1,2,3,4,5}
# c={4,5,6}
# d={5,6,7}
# print(a.isdisjoint(b))#false
# print(a.isdisjoint(c))#True
# print(b.isdisjoint(c))#false
# # print(a.isdisjoint(d))#True
# a={1,2,3}
# b={1,2,3,4,5}
# c={1,2,4,5}
# print(a.issubset(b))#True
# print(b.issubset(a))#False
# # print(a.issubset(c))#False
# print(c.issubset(b))#True
# a={5,1,15,18,20}
# b={15,18,21,25}
# a.difference_update(b)#{5,12,20}
# # b.difference_update(a)#{15,18,21,25}
