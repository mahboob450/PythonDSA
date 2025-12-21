li = [3,1,2,4,1,5,2,6,4]
n = len(li)

def merge(li, low, mid, high):
    ans = []
    left = low
    right = mid + 1
    
    while left <= mid and right <= high:
        if li[left] <= li[right]:
            ans.append(li[left])
            left += 1
        else:
            ans.append(li[right])
            right += 1
    
    while left <= mid:
        ans.append(li[left])
        left += 1
    
    while right <= high:
        ans.append(li[right])
        right += 1
    
    # copy back to original array
    for i in range(len(ans)):
        li[low + i] = ans[i]

def mergeSort(li, low, high):
    if low >= high:
        return
    
    mid = (low + high) // 2
    
    mergeSort(li, low, mid)
    mergeSort(li, mid + 1, high)
    
    merge(li, low, mid, high)

mergeSort(li, 0, n - 1)
print(li)
