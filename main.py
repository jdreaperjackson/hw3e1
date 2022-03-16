from typing import List

# algorithm to compute the median of two sorted arrays using partitioning
def compute_median(arr_a: List[int], arr_b: List[int]) -> float:
    total = len(arr_a) + len(arr_b)
    half = total // 2

    # only necessary to run binary search on one of the arrays
    # if one array is smaller run binary search on that array

    # compare arrays to see if one is smaller
    if len(arr_b) < len(arr_a): # if one array is smaller then assign to a
        arr_a, arr_b = arr_b, arr_a

    # run binary search on a
    l, r = 0, len(arr_a) - 1
    while True:
        i = (l + r) // 2 # pointer for a
        # j is index of the midpoint of b
        j = half - i - 2 # pointer for b

        # handling out of bounds cases
        a_left = arr_a[i] if i >= 0 else float("-infinity")
        a_right = arr_a[i + 1] if (i + 1) < len(arr_a) else float("infinity")
        b_left = arr_b[j] if j >= 0 else float("-infinity")
        b_right = arr_b[j + 1] if (j + 1) < len(arr_b) else float("infinity")

        if a_left <= b_right and b_left <= a_right: # correct partition found
            if total % 2: # odd case
                return min(a_right, b_right)
            return (max(a_left, b_left) + min(a_right, b_right)) / 2 # finding average for even case
        elif a_left > b_right:
            r = i - 1 # move partition one left
        else:
            l = i + 1 # move partition one right


print(compute_median([1, 3, 4, 7, 10], [2, 3, 6, 15]))
