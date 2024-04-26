def BucketSort(array):
    bucket = []

    for i in range(len(array)):
        bucket.append([])

    for j in array:
        index_b = int(10*j)
        bucket[index_b].append(j)

    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    k=0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return  array

def sorted(b):
    for i in range (1,len(b)):
        up = b[i]
        j = i-1
        while j>= 0 and b[j] > up:
            b[j+1] = b[j]
            j -= 1
        b[j+i] = up
    return b