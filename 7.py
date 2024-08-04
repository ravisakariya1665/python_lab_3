def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
elements = [22, 13, 4, 8, 17, 26, 53, 4]
insertion_sort(elements)
print("Sorted elements:", elements)
