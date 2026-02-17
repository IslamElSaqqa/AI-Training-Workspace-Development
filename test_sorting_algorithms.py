"""
test_sorting_algorithms.py
Comprehensive pytest test suite for sorting algorithms.
Tests: QuickSort (recursive & iterative), MergeSort, HeapSort, and built-in sorted()

Run with: pytest test_sorting_algorithms.py -v
"""

import sys
import pytest
from sorting_algorithms import SortAlgorithms

# raise recursion limit to handle deep recursions during QuickSort tests
sys.setrecursionlimit(3000)


class TestEmptyArrays:
    """Test handling of empty arrays."""
    
    def test_quick_sort_recursive_empty(self):
        arr = []
        SortAlgorithms.quick_sort_recursive(arr)
        assert arr == []
    
    def test_quick_sort_iterative_empty(self):
        arr = []
        SortAlgorithms.quick_sort_iterative(arr)
        assert arr == []
    
    def test_merge_sort_empty(self):
        arr = []
        SortAlgorithms.merge_sort(arr)
        assert arr == []
    
    def test_heap_sort_empty(self):
        arr = []
        SortAlgorithms.heap_sort(arr)
        assert arr == []
    
    def test_built_in_sort_empty(self):
        arr = []
        SortAlgorithms.built_in_sort(arr)
        assert arr == []


class TestSingleElement:
    """Test handling of single element arrays."""
    
    def test_quick_sort_recursive_single(self):
        arr = [42]
        SortAlgorithms.quick_sort_recursive(arr)
        assert arr == [42]
    
    def test_quick_sort_iterative_single(self):
        arr = [42]
        SortAlgorithms.quick_sort_iterative(arr)
        assert arr == [42]
    
    def test_merge_sort_single(self):
        arr = [42]
        SortAlgorithms.merge_sort(arr)
        assert arr == [42]
    
    def test_heap_sort_single(self):
        arr = [42]
        SortAlgorithms.heap_sort(arr)
        assert arr == [42]
    
    def test_built_in_sort_single(self):
        arr = [42]
        SortAlgorithms.built_in_sort(arr)
        assert arr == [42]


class TestTwoElements:
    """Test handling of two element arrays."""
    
    def test_quick_sort_recursive_two_elements(self):
        arr = [2, 1]
        SortAlgorithms.quick_sort_recursive(arr)
        assert arr == [1, 2]
    
    def test_merge_sort_two_elements(self):
        arr = [2, 1]
        SortAlgorithms.merge_sort(arr)
        assert arr == [1, 2]
    
    def test_heap_sort_two_elements_unsorted(self):
        arr = [2, 1]
        SortAlgorithms.heap_sort(arr)
        assert arr == [1, 2]
    
    def test_two_elements_already_sorted(self):
        arr = [1, 2]
        SortAlgorithms.quick_sort_iterative(arr)
        assert arr == [1, 2]


class TestAlreadySorted:
    """Test arrays that are already sorted (best case)."""
    
    def test_quick_sort_recursive_sorted(self):
        arr = [1, 2, 3, 4, 5]
        SortAlgorithms.quick_sort_recursive(arr)
        assert arr == [1, 2, 3, 4, 5]
    
    def test_quick_sort_iterative_sorted(self):
        arr = [1, 2, 3, 4, 5]
        SortAlgorithms.quick_sort_iterative(arr)
        assert arr == [1, 2, 3, 4, 5]
    
    def test_merge_sort_sorted(self):
        arr = [1, 2, 3, 4, 5]
        SortAlgorithms.merge_sort(arr)
        assert arr == [1, 2, 3, 4, 5]
    
    def test_heap_sort_sorted(self):
        arr = [1, 2, 3, 4, 5]
        SortAlgorithms.heap_sort(arr)
        assert arr == [1, 2, 3, 4, 5]
    
    def test_built_in_sort_sorted(self):
        arr = [1, 2, 3, 4, 5]
        SortAlgorithms.built_in_sort(arr)
        assert arr == [1, 2, 3, 4, 5]


class TestReverseSorted:
    """Test reverse sorted arrays (worst case for QuickSort)."""
    
    def test_quick_sort_recursive_reverse(self):
        arr = [5, 4, 3, 2, 1]
        SortAlgorithms.quick_sort_recursive(arr)
        assert arr == [1, 2, 3, 4, 5]
    
    def test_quick_sort_iterative_reverse(self):
        arr = [5, 4, 3, 2, 1]
        SortAlgorithms.quick_sort_iterative(arr)
        assert arr == [1, 2, 3, 4, 5]
    
    def test_merge_sort_reverse(self):
        arr = [5, 4, 3, 2, 1]
        SortAlgorithms.merge_sort(arr)
        assert arr == [1, 2, 3, 4, 5]
    
    def test_heap_sort_reverse(self):
        arr = [5, 4, 3, 2, 1]
        SortAlgorithms.heap_sort(arr)
        assert arr == [1, 2, 3, 4, 5]


class TestUnsortedArrays:
    """Test general unsorted arrays."""
    
    def test_quick_sort_recursive_unsorted(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        SortAlgorithms.quick_sort_recursive(arr)
        assert arr == [11, 12, 22, 25, 34, 64, 90]
    
    def test_quick_sort_iterative_unsorted(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        SortAlgorithms.quick_sort_iterative(arr)
        assert arr == [11, 12, 22, 25, 34, 64, 90]
    
    def test_merge_sort_unsorted(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        SortAlgorithms.merge_sort(arr)
        assert arr == [11, 12, 22, 25, 34, 64, 90]
    
    def test_heap_sort_unsorted(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        SortAlgorithms.heap_sort(arr)
        assert arr == [11, 12, 22, 25, 34, 64, 90]
    
    def test_built_in_sort_unsorted(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        SortAlgorithms.built_in_sort(arr)
        assert arr == [11, 12, 22, 25, 34, 64, 90]


class TestDuplicates:
    """Test arrays with duplicate elements."""
    
    def test_quick_sort_recursive_duplicates(self):
        arr = [5, 2, 8, 2, 5, 1, 5]
        SortAlgorithms.quick_sort_recursive(arr)
        assert arr == [1, 2, 2, 5, 5, 5, 8]
    
    def test_quick_sort_iterative_duplicates(self):
        arr = [5, 2, 8, 2, 5, 1, 5]
        SortAlgorithms.quick_sort_iterative(arr)
        assert arr == [1, 2, 2, 5, 5, 5, 8]
    
    def test_merge_sort_duplicates(self):
        arr = [5, 2, 8, 2, 5, 1, 5]
        SortAlgorithms.merge_sort(arr)
        assert arr == [1, 2, 2, 5, 5, 5, 8]
    
    def test_heap_sort_duplicates(self):
        arr = [5, 2, 8, 2, 5, 1, 5]
        SortAlgorithms.heap_sort(arr)
        assert arr == [1, 2, 2, 5, 5, 5, 8]
    
    def test_all_duplicates_quick_sort(self):
        arr = [7, 7, 7, 7, 7]
        SortAlgorithms.quick_sort_recursive(arr)
        assert arr == [7, 7, 7, 7, 7]
    
    def test_all_duplicates_merge_sort(self):
        arr = [7, 7, 7, 7, 7]
        SortAlgorithms.merge_sort(arr)
        assert arr == [7, 7, 7, 7, 7]
    
    def test_all_duplicates_heap_sort(self):
        arr = [7, 7, 7, 7, 7]
        SortAlgorithms.heap_sort(arr)
        assert arr == [7, 7, 7, 7, 7]


class TestNegativeNumbers:
    """Test arrays with negative numbers."""
    
    def test_quick_sort_recursive_negative(self):
        arr = [-1, 5, -3, 0, 2, -10, 8]
        SortAlgorithms.quick_sort_recursive(arr)
        assert arr == [-10, -3, -1, 0, 2, 5, 8]
    
    def test_quick_sort_iterative_negative(self):
        arr = [-1, 5, -3, 0, 2, -10, 8]
        SortAlgorithms.quick_sort_iterative(arr)
        assert arr == [-10, -3, -1, 0, 2, 5, 8]
    
    def test_merge_sort_negative(self):
        arr = [-1, 5, -3, 0, 2, -10, 8]
        SortAlgorithms.merge_sort(arr)
        assert arr == [-10, -3, -1, 0, 2, 5, 8]
    
    def test_heap_sort_negative(self):
        arr = [-1, 5, -3, 0, 2, -10, 8]
        SortAlgorithms.heap_sort(arr)
        assert arr == [-10, -3, -1, 0, 2, 5, 8]
    
    def test_all_negative_quick_sort(self):
        arr = [-5, -1, -10, -3]
        SortAlgorithms.quick_sort_recursive(arr)
        assert arr == [-10, -5, -3, -1]


class TestLargeDatasets:
    """Test with large datasets."""
    
    def test_quick_sort_recursive_1000_elements(self):
        arr = list(range(1000, 0, -1))  # 1000 to 1 descending
        SortAlgorithms.quick_sort_recursive(arr)
        assert arr == list(range(1, 1001))
        assert SortAlgorithms.is_sorted(arr)
    
    def test_quick_sort_iterative_1000_elements(self):
        arr = list(range(1000, 0, -1))
        SortAlgorithms.quick_sort_iterative(arr)
        assert len(arr) == 1000
        assert SortAlgorithms.is_sorted(arr)
        assert arr[0] == 1
        assert arr[-1] == 1000
    
    def test_merge_sort_1000_elements(self):
        arr = list(range(1000, 0, -1))
        SortAlgorithms.merge_sort(arr)
        assert len(arr) == 1000
        assert SortAlgorithms.is_sorted(arr)
        assert arr[0] == 1
        assert arr[-1] == 1000
    
    def test_heap_sort_1000_elements(self):
        arr = list(range(1000, 0, -1))
        SortAlgorithms.heap_sort(arr)
        assert len(arr) == 1000
        assert SortAlgorithms.is_sorted(arr)
        assert arr[0] == 1
        assert arr[-1] == 1000
    
    def test_built_in_sort_1000_elements(self):
        arr = list(range(1000, 0, -1))
        SortAlgorithms.built_in_sort(arr)
        assert len(arr) == 1000
        assert SortAlgorithms.is_sorted(arr)


class TestVeryLargeDatasets:
    """Test with very large datasets."""
    
    def test_quick_sort_iterative_10000_elements(self):
        arr = [(i * 7) % 10000 for i in range(10000)]
        SortAlgorithms.quick_sort_iterative(arr)
        assert SortAlgorithms.is_sorted(arr)
        assert len(arr) == 10000
    
    def test_merge_sort_10000_elements(self):
        arr = [(i * 7) % 10000 for i in range(10000)]
        SortAlgorithms.merge_sort(arr)
        assert SortAlgorithms.is_sorted(arr)
        assert len(arr) == 10000
    
    def test_heap_sort_10000_elements(self):
        arr = [(i * 7) % 10000 for i in range(10000)]
        SortAlgorithms.heap_sort(arr)
        assert SortAlgorithms.is_sorted(arr)
        assert len(arr) == 10000


class TestCrossAlgorithmConsistency:
    """Verify all algorithms produce identical results."""
    
    def test_consistency_random_unsorted(self):
        original = [42, 15, 78, 3, 99, 45, 20, 52]
        
        arr1 = SortAlgorithms.copy_array(original)
        arr2 = SortAlgorithms.copy_array(original)
        arr3 = SortAlgorithms.copy_array(original)
        arr4 = SortAlgorithms.copy_array(original)
        arr5 = SortAlgorithms.copy_array(original)
        
        SortAlgorithms.quick_sort_recursive(arr1)
        SortAlgorithms.quick_sort_iterative(arr2)
        SortAlgorithms.merge_sort(arr3)
        SortAlgorithms.heap_sort(arr4)
        SortAlgorithms.built_in_sort(arr5)
        
        assert arr1 == arr2 == arr3 == arr4 == arr5
    
    def test_consistency_duplicates(self):
        original = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        
        arr1 = SortAlgorithms.copy_array(original)
        arr2 = SortAlgorithms.copy_array(original)
        arr3 = SortAlgorithms.copy_array(original)
        arr4 = SortAlgorithms.copy_array(original)
        
        SortAlgorithms.quick_sort_recursive(arr1)
        SortAlgorithms.merge_sort(arr2)
        SortAlgorithms.heap_sort(arr3)
        SortAlgorithms.built_in_sort(arr4)
        
        assert arr1 == arr2 == arr3 == arr4
    
    def test_consistency_negative_numbers(self):
        original = [-5, 10, -3, 7, 0, -1, 15]
        
        arr1 = SortAlgorithms.copy_array(original)
        arr2 = SortAlgorithms.copy_array(original)
        arr3 = SortAlgorithms.copy_array(original)
        arr4 = SortAlgorithms.copy_array(original)
        
        SortAlgorithms.quick_sort_iterative(arr1)
        SortAlgorithms.merge_sort(arr2)
        SortAlgorithms.heap_sort(arr3)
        SortAlgorithms.built_in_sort(arr4)
        
        assert arr1 == arr2 == arr3 == arr4


class TestEdgeCases:
    """Test edge cases and boundary conditions."""
    
    def test_large_and_small_values_mix(self):
        arr1 = [1000000, -1000000, 0, 1, -1]
        arr2 = SortAlgorithms.copy_array(arr1)
        arr3 = SortAlgorithms.copy_array(arr1)
        
        SortAlgorithms.quick_sort_recursive(arr1)
        SortAlgorithms.merge_sort(arr2)
        SortAlgorithms.heap_sort(arr3)
        
        expected = [-1000000, -1, 0, 1, 1000000]
        assert arr1 == expected
        assert arr2 == expected
        assert arr3 == expected
    
    def test_single_large_value(self):
        arr = [1000000]
        SortAlgorithms.quick_sort_recursive(arr)
        assert arr == [1000000]
    
    def test_two_different_values(self):
        arr1 = [2, 1]
        arr2 = [2, 1]
        arr3 = [2, 1]
        
        SortAlgorithms.quick_sort_iterative(arr1)
        SortAlgorithms.merge_sort(arr2)
        SortAlgorithms.heap_sort(arr3)
        
        assert arr1 == arr2 == arr3 == [1, 2]
    
    def test_many_duplicates_few_unique(self):
        arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1]
        SortAlgorithms.quick_sort_recursive(arr)
        assert arr == [1, 1, 1, 1, 2, 2, 3, 3, 3, 3]


class TestIsSorted:
    """Test the is_sorted utility function."""
    
    def test_is_sorted_empty(self):
        assert SortAlgorithms.is_sorted([]) is True
    
    def test_is_sorted_single(self):
        assert SortAlgorithms.is_sorted([1]) is True
    
    def test_is_sorted_true(self):
        assert SortAlgorithms.is_sorted([1, 2, 3, 4, 5]) is True
    
    def test_is_sorted_false(self):
        assert SortAlgorithms.is_sorted([1, 3, 2, 4, 5]) is False
    
    def test_is_sorted_with_duplicates(self):
        assert SortAlgorithms.is_sorted([1, 2, 2, 3, 3, 3]) is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
