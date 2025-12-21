
li=[8,1,3,2,4,5,7]
n=len(li)
isSorted=True
def bubbleSort(li,n):
    for i in range(n-1):
        for j in range(n-1-i):
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                isSorted=False
        if isSorted:
            break        

    return li


print(f"Before sorting {li}")
bubbleSort(li,n)   
print(f"After sorting {li}")             