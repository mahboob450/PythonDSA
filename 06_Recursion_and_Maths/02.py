# Print 1 to 10 using recursion

# def fun(n):
#     # base case
#     if n==0:
#         return 
#     fun(n-1)
#     print(n)

# fun(10)    
# print("Facrorial")
# def fact(n):
#     if n==1 or n==0:
#         return 1
#     return n*fact(n-1)    
# ans=fact(5)  
# print(ans)  

#  gcd using recursion
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)    

print(gcd(21,70))

def pow(a,b):
    if b==0:
        return 1
    return a*pow(a,b-1) 

result=pow(2,5)
print(result)

#  check prime number

# def isPrime(n):
#     if n==0 or n==1:
#         return false
#     for i in range(2,n):
#         if n%i==0:
#             return false 
#     return True

# print(isPrime(7))               

#  Better approach
from math import sqrt

# def checkPrime(n):
#     cnt=0
#     for i in range(1,int(sqrt(n)+1)):

#         if n%i==0:
#             cnt+=1
#             if (n/i)!=i :
#                 cnt+=1
#     return cnt==2

# print(checkPrime(8))    

def isPrime(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0:
            return False
        return True

print(isPrime(13))
print(isPrime(20))        

# leetcode practice problrm-> 167,151,54,283,121,125 ,217,14,242,48,53,509,231,50
# 




