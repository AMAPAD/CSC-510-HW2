def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        lowestIndex = i
        for j in range(n):
            if arr[j] < arr[lowestIndex]:
                lowestIndex = j

        arr[lowestIndex] = arr[i]
        arr[i] = arr[lowestIndex]
        n = n - 1

    return arr

arr_in = [5, 3, 2, 1, 8, 10, 11, 9, 23]

arr_out = selectionSort(arr_in)

print(arr_out)
