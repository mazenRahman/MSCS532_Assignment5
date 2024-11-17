import random

def randomized_quicksort(arr):
    """
    Randomized Quicksort algorithm implementation.

    Args:
        arr (list): List of elements to sort.

    Returns:
        list: Sorted list.
    """
    if len(arr) <= 1:
        return arr  # Base case: An array of size 0 or 1 is already sorted.
    
    # Step 1: Randomly select a pivot
    pivot_index = random.randint(0, len(arr) - 1)  # Random index within the array
    pivot = arr[pivot_index]  # Choose pivot using the random index
    
    # Step 2: Partition the array
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    # Step 3: Recursively sort the subarrays
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

# Example usage with test cases
if __name__ == "__main__":
    # Test case 1: Unsorted array with unique elements
    array1 = [3, 6, 8, 10, 1, 2, 1]
    print("Test Case 1:")
    print("Original array:", array1)
    print("Sorted array:", randomized_quicksort(array1))
    print()

    # Test case 2: Array with duplicate elements
    array2 = [5, 3, 8, 6, 2, 2, 9, 1, 5]
    print("Test Case 2:")
    print("Original array:", array2)
    print("Sorted array:", randomized_quicksort(array2))
    print()
