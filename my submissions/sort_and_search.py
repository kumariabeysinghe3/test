num_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

#As list is unsorted use linear searching method
#Implement linear searching method on list to look for number 9 
def linear_search(list, target):
    for index, value in enumerate(list):
        if value == target:
            return index 
    return None

print(f"Linear searching method has revealed number 9 to be at index {linear_search(num_list, 9)}")

#perform insertion method searching on num_list
def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        # Move elements greater than key one position ahead
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list

# Sort the list
sorted_numbers = insertion_sort(num_list.copy())
print("Sorted list:", sorted_numbers)

#perform last step, binary sorting. You would use this type of sorting method with sorted data in the real world such as dictionaries
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print("Binary search: Number 9 found at index", binary_search(sorted_numbers, 9))