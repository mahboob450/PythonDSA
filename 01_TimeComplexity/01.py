# Time comlexity in coputer science describes how the execution time of an algorithm grows as the input size increses.
# It essentially quantifies the number of operations an algorithm performs as a function of the input size. 

# ASYMPTOTIC NOTATION:
# Big O Notation (O): Describes the upper bound of an algorithm's time complexity. It provides a worst-case scenario for how the execution time grows with input size.
# Omega Notation (Ω): Describes the lower bound of an algorithm's time complexity. It provides a best-case scenario for how the execution time grows with input size.
# Theta Notation (Θ): Describes the tight bound of an algorithm's time complexity
# It provides an average-case scenario for how the execution time grows with input size.

# COMMON TIME COMPLEXITIES:
# O(1) - Constant Time: The execution time remains constant regardless of the input size.
def constant_time_example(arr):
    return arr[0]  # Accessing the first element takes constant time.   
# O(log n) - Logarithmic Time: The execution time grows logarithmically with the input size.
def logarithmic_time_example(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Target not found   
# O(n) - Linear Time: The execution time grows linearly with the input size.

def linear_time_example(arr):
    total = 0
    for num in arr:
        total += num  # Summing all elements takes linear time.
    return total
# O(n log n) - Linearithmic Time: The execution time grows in proportion to n log n.
def linearithmic_time_example(arr):
    return sorted(arr)  # Sorting using Timsort has a time complexity of O(n log n).
# O(n^2) - Quadratic Time: The execution time grows quadratically with the input size.

def quadratic_time_example(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            count += 1  # Nested loops result in quadratic time complexity.
    return count
# O(2^n) - Exponential Time: The execution time doubles with each additional input element.
def exponential_time_example(n):
    if n == 0:
        return 1
    else:
        return exponential_time_example(n - 1) + exponential_time_example(n - 1)  # Exponential growth.
# O(n!) - Factorial Time: The execution time grows factorially with the input size.

def factorial_time_example(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_time_example(n - 1)  # Factorial growth.
    
# comparasion of time complexities:
# O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)  

# space complexity:
# Space complexity in computer science describes how the memory usage of an algorithm grows as the input size increases.
# It quantifies the amount of memory an algorithm requires as a function of the input size.
# Common Space Complexities:
# O(1) - Constant Space: The memory usage remains constant regardless of the input size.
def constant_space_example(arr):
    return arr[0]  # Accessing the first element uses constant space.
# O(n) - Linear Space: The memory usage grows linearly with the input size.
def linear_space_example(n):
    arr = [0] * n  # Creating an array of size n uses linear space.
    return arr
# O(n^2) - Quadratic Space: The memory usage grows quadratically with the input size.
def quadratic_space_example(n):
    matrix = [[0] * n for _ in range(n)]  # Creating an n x n matrix uses quadratic space.
    return matrix
# O(log n) - Logarithmic Space: The memory usage grows logarithmically with the input size.
def logarithmic_space_example(n):
    if n <= 1:
        return 1
    else:
        return logarithmic_space_example(n // 2) + 1  # Logarithmic space usage due to recursion.
# O(n log n) - Linearithmic Space: The memory usage grows in proportion to n log n.
def linearithmic_space_example(n):
    arr = [0] * n
    arr.sort()  # Sorting may use O(n log n) space in some algorithms.
    return arr
# O(2^n) - Exponential Space: The memory usage doubles with each additional input element.
def exponential_space_example(n):
    if n == 0:
        return [[]]  # Base case uses constant space.
    else:
        subsets = exponential_space_example(n - 1)
        return subsets + [s + [n - 1] for s in subsets]  # Exponential space usage.
# O(n!) - Factorial Space: The memory usage grows factorially with the input size.

def factorial_space_example(n):
    if n == 0:
        return [[]]  # Base case uses constant space.
    else:
        permutations = factorial_space_example(n - 1)
        result = []
        for p in permutations:
            for i in range(len(p) + 1):
                result.append(p[:i] + [n - 1] + p[i:])  # Factorial space usage.
        return result
# comparasion of space complexities:
# O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)



z={}

