def merge_list(list1, list2):
    # Check if both inputs are lists
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Both inputs must be lists")

    # Check if the lists contain only integers
    if not all(isinstance(item, int) for item in list1) or not all(isinstance(item, int) for item in list2):
        raise TypeError("Lists must only contain integers")

    # Merge the two lists
    merged_list = list1 + list2

    # Perform a simple merge sort (you can also use other sorting algorithms)
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

        merged = []
        left_index = 0
        right_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                merged.append(left_half[left_index])
                left_index += 1
            else:
                merged.append(right_half[right_index])
                right_index += 1

        merged += left_half[left_index:]
        merged += right_half[right_index:]

        return merged

    merged_list = merge_sort(merged_list)

    return merged_list



