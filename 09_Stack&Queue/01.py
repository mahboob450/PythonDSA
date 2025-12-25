# Introduction to stack data structure
#  stack is a linear data structure that follow LIFO Priciple , the last elemnent inserted is tha first to be popped out.
#  Basic operations of stack -> push, pop, top,isEmpty,isFull


#  Array implementation of stack:-
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def __iter__(self):  #__iter__() ek special (dunder) method hai
        # 👉 Python ise automatically call karta hai jab:
        # for loop use hota hai
        # list(), tuple() me convert karte ho
        # in keyword use karte ho
        return iter(self.items)


st = Stack()
st.push(10)
st.push(13)
st.push(105)
st.push(102)
st.push(12)

# for i in st:
#     print(i)
print(st.top())  

# leetcode 20,496