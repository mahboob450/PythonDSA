li=[5,4,3,2,1]
n=len(li)

def selectionSort(li,n):
    for i in range(n-1):
        mini=li[i]
        idx=i
        for j in range(i,n):
            if mini>li[j]:
                mini=li[j]
                idx=j
        li[idx],li[i]=li[i],li[idx]        

selectionSort(li,n)
print(li)
