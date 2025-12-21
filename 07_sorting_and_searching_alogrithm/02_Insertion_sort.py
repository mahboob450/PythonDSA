li=[5,4,3,2,1]
n=len(li)

def insertionSort(li,n):
    for i in range(1,n):
        j=i
        while j>0 and li[j-1]>li[j] :
            li[j-1],li[j] = li[j],li[j-1]
            j-=1
    return li
print(f"Before sorting {li}")
insertionSort(li,n)
print(f"After sorting {li}")            