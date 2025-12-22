# What is Linear Search?
# Linear search is the simplest search algorithm:
# It searches for an element in a list (or array) one by one from the start.
# If it finds the element, it returns its index.
# If the element is not found, it returns -1 or some indication of “not found”.

# Time Complexity:

# Best case: O(1)
# O(1) → element is at the start.

# Worst case: O(n)
# O(n) → element is at the end or not present.

# Space Complexity: O(1)
# O(1) → no extra space needed.

li=[1,23,12,11,10,9,6,7]
n=len(li)

def findTarget(target):
    for i in range(n):
        if li[i]==target:
            return True

    return False
print(findTarget(10))           