# dictionary-> A dictionary in Python is a collection of key–value pairs.
# It is unordered, mutable, and indexed by keys.

dict1={1:"mahboob", 2:"raj" , 3:"Mukesh"}
print(dict1)
print(type(dict1))
print(len(dict1))
print(dict1[1])
dict1[1]="rishu"
print(dict1)
dict1.update({10:"hellow",11:"hii"})
print(dict1)

dict1.pop(10)
print(dict1)

dict2={1:"Abhinav",2:"Abhishek",3:"Sakshi",4:"Sharish"}

# for i in dict2:
#     print(i,dict2[i])

for i in dict2.keys():
    print(i,dict2[i])   

for i in dict2.values():
    print(i)

print(list(dict2.values()))       

print(dict2.items())

# frequency of element in a list (important)
list1=[2,3,4,1,2,3,4,5,4,3,2]

freq={}

for i in list1:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1    

for i in freq:
    print(f"{i} is present {freq[i]} times")    

# freq.get(key, default)
# If key exists → returns its value
# If key does NOT exist → returns default    

#Two sum -Array is unsorted  ..dictionary is used