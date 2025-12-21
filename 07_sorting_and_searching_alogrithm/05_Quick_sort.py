li = [4,6,2,5,7,9,1,3]
n = len(li)

def partionIdx(li, low, high):
    pivot = li[low]
    i = low + 1  # start right after pivot
    j = high

    while i <= j:
        while i <= high and li[i] <= pivot:
            i += 1
        while j >= low and li[j] > pivot:
            j -= 1

        if i < j:
            li[i], li[j] = li[j], li[i]

    # Swap pivot into correct position
    li[low], li[j] = li[j], li[low]
    return j

def quickSort(li, low, high):
    if low < high:
        idx = partionIdx(li, low, high)
        quickSort(li, low, idx - 1)
        quickSort(li, idx + 1, high)

quickSort(li, 0, n - 1)
print(li)

