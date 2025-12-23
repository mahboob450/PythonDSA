# recursion -> A function calling itself until a base condition is met
#  base case -> terminating condition

# def sum(n):
#     if n==0:
#         return 

#     sum(n-1)
#     print("Hellow")   

# sum(10)

#  find sum from 1 to 10 using recursion

def findSum(n):
    if n==1:
        return 1
    return n+findSum(n-1)    

a=findSum(10)   
print(a) 