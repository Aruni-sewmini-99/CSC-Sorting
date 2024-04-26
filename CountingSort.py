def countingSort(array):
    size = len(array)
    output = [0]*size
    max_value = max(array)
    count = [0]*(max_value+1)

    for num in array:
        count[num] +=  1

    for i in range (1, len(count)):
        count[i] += count[i-1]

    for num in array:
        output[count[num]-1] = num
        count[num] -= 1

    return output