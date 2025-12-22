# set -> unique element, unordered, mutable , no indexing

set1={"mahboob",1,1.2,"hii","mahboob"}
print(set1) # {'hii', 1, 'mahboob', 1.2}
print(type(set1))
print(len(set1))

set1.add(100)
print(set1)
# set1.clear()
print(set1)
set1.discard(100) #Ye set se element remove karta hai — lekin agar element na mile tab bhi error nahi deta.
print(set1)

# set operations
#  union
set2={1,2,3,4,5}
set3={3,2,7,9}
print(set2|set3)
s=set2.union(set3)
print(s)

# intersaction
print(set2&set3)

# difference 
print(set2-set3)
print(set2.difference(set3))

#  symmetric_difference=union - intersaction

print(set2^set3)
print(set2.symmetric_difference(set3))