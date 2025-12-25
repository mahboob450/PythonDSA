#linked list-> Linked list is basically chains of nodes where each node contains information such as data and a pointer to the next node in the chain.

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None # Initially none
        print("Node is created!")

a=Node(5)  # a is a node with value five
print(a.data)
print(a.next)
b=Node(6)
c=Node(7)
a.next=b
b.next=c
head=a

print(head.data) #5
print(head.next.data) #6
print(head.next.next.data) #7

#  print linked list

def printLL(head):
    temp=head
    lenghtLL=0
    while temp!=None:
        print(temp.data,end=" ")
        temp=temp.next
        lenghtLL+=1

    return lenghtLL

l=printLL(head)
print(f"Lenght of linked list is {l}")

#  Insertion at starting of linked list

def insertAtHead(head):
    newNode=Node(4)
    newNode.next=head
    head=newNode
    return head

head=insertAtHead(head)
print(head.data)

#  Insertion at the end of the linked list

def insertAtEnd(head):
    newNode=Node(8)
    temp=head
    while temp.next!=None:
        temp=temp.next

    temp.next=newNode  
    return head

head=insertAtEnd(head)
printLL(head)    

#  insertion at specific index

def insertAtSpecificIdx(head,idx):
    temp=head
    newNode=Node(10)
    i=1
    while i<idx:
        i+=1
        temp=temp.next
    newNode.next=temp.next
    temp.next=newNode
    return head

head=insertAtSpecificIdx(head,2)
printLL(head)