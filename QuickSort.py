def quicksort(arr):
    """
    Quicksort algorithm implementation.

    Args:
        arr (list): List of elements to sort.

    Returns:
        list: Sorted list.
    """
    if len(arr) <= 1:
        return arr  # Base case: An array of size 0 or 1 is already sorted.
    
    # Choose the pivot (middle element for simplicity)
    pivot = arr[len(arr) // 2]
    
    # Partition the array
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    # Recursively sort left and right subarrays
    return quicksort(left) + middle + quicksort(right)

# Example usage with test cases
if __name__ == "__main__":
    # Test case 1: Unsorted array with unique elements
    array1 = [3, 6, 8, 10, 1, 2, 1]
    print("Test Case 1:")
    print("Original array:", array1)
    print("Sorted array:", quicksort(array1))
    print()

    # Test case 2: Array with duplicate elements
    array2 = [5, 3, 8, 6, 2, 2, 9, 1, 5]
    print("Test Case 2:")
    print("Original array:", array2)
    print("Sorted array:", quicksort(array2))
    print()

    # Test case 3: Already sorted array
    array3 = [1, 2, 3, 4, 5]
    print("Test Case 3:")
    print("Original array:", array3)
    print("Sorted array:", quicksort(array3))
    print()

    # Test case 4: Reverse sorted array
    array4 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Test Case 4:")
    print("Original array:", array4)
    print("Sorted array:", quicksort(array4))
    print()

    # Test case 5: Array with a single element
    array5 = [42]
    print("Test Case 5:")
    print("Original array:", array5)
    print("Sorted array:", quicksort(array5))
    print()

    # Test case 6: Empty array
    array6 = []
    print("Test Case 6:")
    print("Original array:", array6)
    print("Sorted array:", quicksort(array6))
    print()
