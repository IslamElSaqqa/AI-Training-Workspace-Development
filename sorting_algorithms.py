"""
sorting_algorithms.py
Implements four sorting algorithms:
- QuickSort (recursive and iterative)
- MergeSort
- HeapSort
- Built-in sorted()
"""

class SortAlgorithms:
    """Contains implementations of various sorting algorithms."""

    @staticmethod
    def quick_sort_recursive(arr, low=None, high=None):
        """
        Recursive QuickSort implementation using Lomuto partition scheme with
        randomized pivot to avoid worst-case recursion depth on sorted inputs.
        
        Args:
            arr: List of integers to sort
            low: Start index (default: 0)
            high: End index (default: len(arr) - 1)
        """
        import random, sys
        # ensure recursion limit is sufficiently high for large inputs
        sys.setrecursionlimit(max(sys.getrecursionlimit(), 2000))

        if low is None:
            low = 0
        if high is None:
            high = len(arr) - 1
            
        if low < high:
            # choose random pivot and move it to end before partitioning
            pivot_index = random.randint(low, high)
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

            pivot = SortAlgorithms._partition_quick(arr, low, high)
            SortAlgorithms.quick_sort_recursive(arr, low, pivot - 1)
            SortAlgorithms.quick_sort_recursive(arr, pivot + 1, high)

    @staticmethod
    def quick_sort_iterative(arr):
        """
        Iterative QuickSort using explicit stack to eliminate recursion.
        
        Args:
            arr: List of integers to sort
        """
        if len(arr) <= 1:
            return
        
        stack = []
        stack.append(0)
        stack.append(len(arr) - 1)
        
        while stack:
            high = stack.pop()
            low = stack.pop()
            
            if low < high:
                pivot = SortAlgorithms._partition_quick(arr, low, high)
                
                if pivot + 1 < high:
                    stack.append(pivot + 1)
                    stack.append(high)
                
                if low < pivot - 1:
                    stack.append(low)
                    stack.append(pivot - 1)

    @staticmethod
    def _partition_quick(arr, low, high):
        """
        Partition array using Lomuto partition scheme.
        
        Args:
            arr: Array to partition
            low: Start index
            high: End index (pivot)
            
        Returns:
            Final position of pivot
        """
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    @staticmethod
    def merge_sort(arr):
        """
        MergeSort implementation using divide and conquer.
        
        Args:
            arr: List of integers to sort
        """
        if len(arr) <= 1:
            return
        
        SortAlgorithms._merge_sort_helper(arr, 0, len(arr) - 1)

    @staticmethod
    def _merge_sort_helper(arr, left, right):
        """Helper function for recursive merge sort."""
        if left < right:
            mid = left + (right - left) // 2
            SortAlgorithms._merge_sort_helper(arr, left, mid)
            SortAlgorithms._merge_sort_helper(arr, mid + 1, right)
            SortAlgorithms._merge(arr, left, mid, right)

    @staticmethod
    def _merge(arr, left, mid, right):
        """Merge two sorted subarrays."""
        temp = []
        i, j = left, mid + 1
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        
        while i <= mid:
            temp.append(arr[i])
            i += 1
        
        while j <= right:
            temp.append(arr[j])
            j += 1
        
        for i, val in enumerate(temp):
            arr[left + i] = val

    @staticmethod
    def heap_sort(arr):
        """
        HeapSort implementation using max-heap.
        
        Args:
            arr: List of integers to sort
        """
        n = len(arr)
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            SortAlgorithms._heapify(arr, n, i)
        
        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            SortAlgorithms._heapify(arr, i, 0)

    @staticmethod
    def _heapify(arr, n, i):
        """Maintain max-heap property."""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            SortAlgorithms._heapify(arr, n, largest)

    @staticmethod
    def built_in_sort(arr):
        """
        Python's built-in sort using Timsort.
        
        Args:
            arr: List of integers to sort
        """
        arr.sort()

    @staticmethod
    def copy_array(arr):
        """Create a copy of array."""
        return arr.copy()

    @staticmethod
    def is_sorted(arr):
        """Check if array is sorted."""
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True
