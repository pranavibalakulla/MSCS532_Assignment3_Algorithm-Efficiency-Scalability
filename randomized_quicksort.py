import random

def randomized_quicksort(array, low=0, high=None):

    if high is None:
        high = len(array) - 1  # Initialize high for the first call

    if low < high:
        # Choose a random pivot index within the current subarray
        pivot_index = random.randint(low, high)
        # Move pivot to the end to simplify partitioning
        array[pivot_index], array[high] = array[high], array[pivot_index]

        # Partition the array and get the final pivot position
        p = partition(array, low, high)

        # Recursively sort elements before and after the pivot
        randomized_quicksort(array, low, p - 1)
        randomized_quicksort(array, p + 1, high)

    return array

def partition(array, low, high):
    pivot = array[high]  # Pivot is at the end
    i = low - 1        # Index of smaller element

    # Traverse the subarray and swap elements to ensure correct partition
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    # Place the pivot in its correct position
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def run_quicksort():
    # Generate a list of 10 random integers between 0 and 100
    data = [random.randint(0, 100) for _ in range(10)]

    # Print the original unsorted array
    print("Original array:", data)

    # Apply randomized quicksort and print the sorted result
    print("Sorted array:  ", randomized_quicksort(data))

# Call the function to execute randomized quicksort
run_quicksort()
