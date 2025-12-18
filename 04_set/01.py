# set -> unique element, unordered, mutable

set1={"mahboob",1,1.2,"hii","mahboob"}
print(set1) # {'hii', 1, 'mahboob', 1.2}
print(type(set1))
print(len(set1))

set1.add(100)
print(set1)
set1.clear()
print(set1)