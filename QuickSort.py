def quickSort (array,p,r):
    if p < r:
        q = partition (array, p, r)
        quickSort(array,p,q-1)
        quickSort(array,q+1,r)

def partition(array,p,r):
    pivot = array[r]
    i = p-1

    for j in range(p,r):
        if array[j] <= pivot:
            i=i+1
            (array[i], array[j]) = (array[j],array[i])

        (array[i+1],array[r])  = (array[r],array[i+1])

    return i+1 