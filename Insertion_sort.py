def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j = j - 1


arr = [2, 7, 4, 5, 7, 89, 5, 3, 2]
insertion_sort(arr)
print(arr)
