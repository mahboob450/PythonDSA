class Node:
    def __init__(self,data):
        self.data=data
        self.next=None # Initially none
        

a=Node(5)  # a is a node with value five
b=Node(6)
c=Node(7)
d=Node(8)
a.next=b
b.next=c
c.next=d

head=a

def printLL(head):
    temp=head
    while temp!=None:
        print(temp.data,end=" ")
        temp=temp.next

printLL(head)       
print(" ")
# # delete head:
# def deleteHead(head):
#     temp=head
#     return temp.next

# head=deleteHead(head)
# printLL(head)    
# print()
#  delete tail

# def deleteTail(head):
#     temp=head
#     while temp.next.next!=None:
#         temp=temp.next
#     temp.next=None
#     return head

# head=deleteTail(head)
# printLL(head)       
print()
#  delete at specific index
def deleteAtSpecificIdx(head,idx):
    temp=head
    i=1
    while i<idx:
        i+=1
        temp=temp.next
    temp.next=temp.next.next
    return head

head=deleteAtSpecificIdx(head,2)
printLL(head)

# leetcode-> 876,19,206,141,21,203,2,160,142