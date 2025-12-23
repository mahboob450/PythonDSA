# recursion -> A function calling itself until a base condition is met
#  base case -> terminating condition

def sum(n):
    if n==0:
        return 

    sum(n-1)
    print("Hellow")   

sum(10)