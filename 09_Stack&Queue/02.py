# Introduction to queue data structure:-
#    Queue is a linear data structure that follows FIFO principlee,so tha first element inserted is the first to be popped out.


# leecode 232
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)   # insert at rear

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)   # remove from front

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.front()

print(q.front())     # 10
print(q.dequeue())   # 10
print(q.dequeue())   # 20
print(q.size())      # 1
