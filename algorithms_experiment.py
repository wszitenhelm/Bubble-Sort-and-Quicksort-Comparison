import time
import random
from scipy.stats import ttest_rel
import statistics
import matplotlib.pyplot as plt

import sys
sys.setrecursionlimit(30000)


def bubble_sort_iterative(arr):
    n = len(arr)
    for i in range(n):
        # Optimized: Stop if no swaps occurred
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # If no swaps, array is already sorted
            break
    return arr


def quicksort_recursive(arr):
    # Base case: If the array has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choose the pivot (typically the last element)
    pivot = arr[-1]

    # Partition the array
    left = [x for x in arr[:-1] if x <= pivot]  # Elements less than or equal to the pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements greater than the pivot

    # Recursive sorting of left and right partitions
    sorted_left = quicksort_recursive(left)
    sorted_right = quicksort_recursive(right)

    # Combine the sorted partitions and the pivot
    return sorted_left + [pivot] + sorted_right


# Test sorting functions and store results
def test_sorting_algorithms(datasets):
    results = {}
    for i, dataset in enumerate(datasets):
        dataset_copy = dataset.copy()
        
        # Measure Bubble Sort time
        start = time.perf_counter()
        bubble_sort_iterative(dataset_copy)
        end = time.perf_counter()
        bubble_time = end - start
        
        # Measure Quick Sort time
        dataset_copy = dataset.copy()
        start = time.perf_counter()
        quicksort_recursive(dataset_copy)
        end = time.perf_counter()
        quick_time = end - start
       
        # Save the results
        results[f"dataset_{i+1}"] = {
            "bubble_sort": bubble_time,
            "quick_sort": quick_time
        }
    return results


example_set = []
# Example usage 

tested_set = test_sorting_algorithms(example_set)

# Print results 
for dataset, times in tested_set.items():
    print(f"{dataset}: Bubble Sort = {times['bubble_sort']}s, Quick Sort = {times['quick_sort']}s")


# Extract times for Bubble Sort and QuickSort into separate arrays
bubble_sort_times = [times["bubble_sort"] for times in tested_set.values()]
quick_sort_times = [times["quick_sort"] for times in tested_set.values()]

bubble_sort_times_average = sum(bubble_sort_times)/50 
print("Bubble sort averaga:", bubble_sort_times_average)

quicksort_times_average = sum(quick_sort_times )/50 
print("quicksort_times_average:", quicksort_times_average)

# Perform a paired t-test
t_stat, p_value = ttest_rel(bubble_sort_times, quick_sort_times)

# Print results
print(f"T-statistic: {t_stat}")
print(f"P-value (two-tailed): {p_value}")

# Calculate standard deviation
std_deviation_bubble = statistics.stdev(bubble_sort_times)
std_deviation_quick = statistics.stdev(quick_sort_times)

print("Standard Deviation Bubble Sort:", std_deviation_bubble)
print("Standard Deviation Quick Sort:", std_deviation_quick)

# Create a box plot
plt.boxplot([bubble_sort_times, quick_sort_times], labels=['Bubble Sort', 'Quick Sort'])

# Add title and labels
plt.title('Comparison of Execution Times \n for Large Partially Sorted Datasets')
plt.ylabel('Execution Time (seconds)')

# Show the plot
plt.show()