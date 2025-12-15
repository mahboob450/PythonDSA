# List -> hetrogenious , dynamic size, ordered, mutable,duplicates value

# li=["mahboob",12,12.3,"apple"]
# print(li)
# print(len(li))
# print(type(li))

# Important list function
# function->Independent; does not belong to any object.
# eg “Important list functions include: len, min, max, sum, sorted, and list.

li1=[1,243,23,43,100]
print(len(li1))

print(min(li1))
print(max(li1))
print(sum(li1))
print(sorted(li1)) #Returns a new sorted list.
print(list("abc")) #Converts other iterables into a list. ['a', 'b', 'c']

print(list(range(1,10))) # (start,end,step) end is exclusive -> 1 to n-1
print(list(range(15,9))) # []

print(list(range(10,5,-2))) #[10, 8, 6]
# shallow copy
list2 = [1,2,3]
list3 = list2.copy() # shallow copy -> just copy the value , both point to diff memory location

list2[0] = 100
list3[1] = 100

print(list2,id(list2))
print(list3,id(list3))

# Deep copy
list2 = [1,2,3]
list3 = list2 # deep copy -> refrence same hoga, both list3 and list2 point to same memory location

list2[0] = 100
list3[1] = 100

print(list2,id(list3))
print(list3,id(list3))

#slicin4
list4 = [4,2,4,5,7,2,1,8]

print(list4[2:6])
print(list4[:6])
print(list4[6:])
print(list4[7:1:-2])
# 7,5

print(list4[::-1]) # reverse

# Method ->Dependent; always associated with an object.
# Important list methods include: append, insert, extend, remove, pop, clear, index, count, reverse, and sort.”

li5=[1,2,43,5,3,65]
li5.append(10) #Add item at end
print(li5)
li5.insert(1,20) #Add item at a specific index
li5.extend([45,47]) #Add multiple items 

li5.remove(45) #Remove by value
li5.pop(5) #Remove by index (returns removed item)
li5.clear() #Remove all items
# li5.index(65) #Returns index of an element
li5.count(1) #Count occurrences of a value
li5.reverse() #Reverse the list in place
li5.sort() #Sort list in place-> original list is modified


