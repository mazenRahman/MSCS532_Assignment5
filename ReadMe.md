
 Overview

Quicksort is a highly efficient, divide-and-conquer sorting algorithm that works by:
1. Selecting a pivot element.
2. Partitioning the array into:
   - Elements less than the pivot.
   - Elements equal to the pivot.
   - Elements greater than the pivot.
3. Recursively sorting the partitions.

The implementations provided here include:
- Deterministic Quicksort: Predictable pivot selection (middle element).
- Randomized Quicksort: Random pivot selection for robustness.

---

 Features
- Efficient Sorting: Average-case time complexity of (O(n log n)).
- In-Place Sorting: Minimal auxiliary space.
- Robust Randomization: Reduces the likelihood of worst-case performance.

---

 Usage

# 1. Deterministic Quicksort
The deterministic implementation uses the middle element as the pivot. Example usage:
```python
def quicksort(arr):
    """
    Quicksort algorithm implementation.
    Args:
        arr (list): List of elements to sort.
    Returns:
        list: Sorted list.
    """
```

# 2. Randomized Quicksort
The randomized implementation selects a random pivot. Example usage:
```python
import random

def randomized_quicksort(arr):
    """
    Randomized Quicksort algorithm implementation.
    Args:
        arr (list): List of elements to sort.
    Returns:
        list: Sorted list.
    """
```

---

 Examples

# Deterministic Quicksort
```python
array = [3, 6, 8, 10, 1, 2, 1]
sorted_array = quicksort(array)
print(sorted_array)  # Output: [1, 1, 2, 3, 6, 8, 10]
```

# Randomized Quicksort
```python
array = [5, 3, 8, 6, 2, 2, 9, 1, 5]
sorted_array = randomized_quicksort(array)
print(sorted_array)  # Output: [1, 2, 2, 3, 5, 5, 6, 8, 9]
```

---

 Test Cases

# Deterministic Quicksort
1. Unsorted Array: `[3, 6, 8, 10, 1, 2, 1]`
2. Array with Duplicates: `[5, 3, 8, 6, 2, 2, 9, 1, 5]`
3. Already Sorted Array: `[1, 2, 3, 4, 5]`
4. Reverse-Sorted Array: `[9, 8, 7, 6, 5, 4, 3, 2, 1]`
5. Single Element: `[42]`
6. Empty Array: `[]`

# Randomized Quicksort
Same as above, with improved performance on sorted and reverse-sorted arrays.

---

 Performance

| Input Type        | Deterministic Quicksort | Randomized Quicksort |
|--------------------|-------------------------|-----------------------|
| Random            | (O(n log n))         | (O(n log n))       |
| Sorted            | (O(n^2))              | (O(n log n))       |
| Reverse-Sorted    | (O(n^2))              | (O(n log n))       |

---



