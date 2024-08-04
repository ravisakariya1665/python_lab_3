def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
elements = [1, 3, 5, 8, 10, 23, 35]
search_target = 10
index = sequential_search(elements, search_target)
if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")
