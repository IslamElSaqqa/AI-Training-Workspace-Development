# Pytest Unit Tests for Sorting Algorithms

Comprehensive pytest test suite for all sorting algorithms: QuickSort, MergeSort, HeapSort, and built-in sorted().

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Install pytest

```bash
pip install pytest
```

Or upgrade pytest if already installed:
```bash
pip install --upgrade pytest
```

## Files

1. **sorting_algorithms.py** - Implementation of all four sorting algorithms
2. **test_sorting_algorithms.py** - Comprehensive pytest test suite (~60+ tests)

## Test Coverage

The test suite includes **60+ unit tests** covering:

### Test Categories:

- ✅ **Empty Arrays (5 tests)** - Edge case: no elements
- ✅ **Single Element (5 tests)** - Minimal array
- ✅ **Two Elements (4 tests)** - Smallest sorting scenario
- ✅ **Already Sorted (5 tests)** - Best case scenario
- ✅ **Reverse Sorted (5 tests)** - Worst case for QuickSort
- ✅ **Unsorted Arrays (5 tests)** - General random data
- ✅ **Duplicates (7 tests)** - Arrays with repeated elements
- ✅ **Negative Numbers (5 tests)** - Mixed positive/negative
- ✅ **Large Datasets (5 tests)** - 1,000 elements
- ✅ **Very Large Datasets (3 tests)** - 10,000 elements
- ✅ **Cross-Algorithm Consistency (3 tests)** - All algorithms produce same result
- ✅ **Edge Cases (5 tests)** - Boundary values and special cases
- ✅ **Utility Tests (5 tests)** - Helper functions

## Running Tests

### Run All Tests (Verbose Output)

```bash
pytest test_sorting_algorithms.py -v
```

### Run Specific Test Class

```bash
pytest test_sorting_algorithms.py::TestEmptyArrays -v
```

### Run Specific Test

```bash
pytest test_sorting_algorithms.py::TestUnsortedArrays::test_quick_sort_recursive_unsorted -v
```

### Run with Coverage Report

```bash
pip install pytest-cov
pytest test_sorting_algorithms.py --cov=sorting_algorithms --cov-report=html
```

This generates an HTML coverage report in `htmlcov/index.html`

### Run with Markers (Filter Tests)

```bash
# Run only QuickSort tests
pytest test_sorting_algorithms.py -k "quick_sort" -v

# Run only MergeSort tests
pytest test_sorting_algorithms.py -k "merge_sort" -v

# Run only HeapSort tests
pytest test_sorting_algorithms.py -k "heap_sort" -v
```

### Run Tests with Output Detail

```bash
# Show print statements
pytest test_sorting_algorithms.py -v -s

# Show local variables on failure
pytest test_sorting_algorithms.py -v -l

# Stop on first failure
pytest test_sorting_algorithms.py -v -x
```

### Run Tests in Parallel (Faster)

```bash
pip install pytest-xdist
pytest test_sorting_algorithms.py -v -n auto
```

## Expected Output

A successful test run shows:

```
test_sorting_algorithms.py::TestEmptyArrays::test_quick_sort_recursive_empty PASSED
test_sorting_algorithms.py::TestEmptyArrays::test_quick_sort_iterative_empty PASSED
test_sorting_algorithms.py::TestEmptyArrays::test_merge_sort_empty PASSED
...
======================== 60 passed in 0.45s ========================
```

## Test Organization

### Test Classes:

1. **TestEmptyArrays** - Handling of empty input
2. **TestSingleElement** - Single-element arrays
3. **TestTwoElements** - Two-element arrays
4. **TestAlreadySorted** - Pre-sorted data (best case)
5. **TestReverseSorted** - Reverse-sorted data (worst case)
6. **TestUnsortedArrays** - Random unsorted data
7. **TestDuplicates** - Arrays with duplicate elements
8. **TestNegativeNumbers** - Mixed positive/negative values
9. **TestLargeDatasets** - 1,000+ elements
10. **TestVeryLargeDatasets** - 10,000+ elements
11. **TestCrossAlgorithmConsistency** - Verify all algorithms produce identical results
12. **TestEdgeCases** - Boundary values and special scenarios
13. **TestIsSorted** - Utility function validation

## Supported Algorithms

### 1. QuickSort Recursive
- Method: `SortAlgorithms.quick_sort_recursive(arr)`
- Time: O(n log n) avg, O(n²) worst
- Space: O(log n) avg, O(n) worst
- Stable: No

### 2. QuickSort Iterative
- Method: `SortAlgorithms.quick_sort_iterative(arr)`
- Time: O(n log n) avg, O(n²) worst
- Space: O(log n) avg, O(n) worst
- Stable: No

### 3. MergeSort
- Method: `SortAlgorithms.merge_sort(arr)`
- Time: O(n log n) guaranteed
- Space: O(n)
- Stable: Yes

### 4. HeapSort
- Method: `SortAlgorithms.heap_sort(arr)`
- Time: O(n log n) guaranteed
- Space: O(1)
- Stable: No

### 5. Built-in Sort
- Method: `SortAlgorithms.built_in_sort(arr)`
- Uses Python's Timsort (hybrid algorithm)
- Time: O(n) best, O(n log n) avg/worst
- Space: O(n)
- Stable: Yes

## Assertions and Methods

### Array Assertions:
```python
assert arr == expected_array  # Compare arrays
assert SortAlgorithms.is_sorted(arr)  # Check if sorted
```

### Utility Methods:
```python
SortAlgorithms.copy_array(arr)  # Create array copy
SortAlgorithms.is_sorted(arr)   # Verify sorting
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'pytest'"
```bash
pip install pytest
```

### "ModuleNotFoundError: No module named 'sorting_algorithms'"
- Ensure both files are in the same directory
- Or add the directory to PYTHONPATH:
  ```bash
  export PYTHONPATH="${PYTHONPATH}:$(pwd)"  # Linux/Mac
  set PYTHONPATH=%PYTHONPATH%;%cd%  # Windows
  ```

### Tests Running Slowly
- Use parallel execution: `pytest -n auto`
- Run specific test class instead of all tests

### Out of Memory on Very Large Tests
- Skip very large dataset tests: `pytest -k "not VeryLarge"`
- Reduce dataset sizes in test file

## Integration with CI/CD

### GitHub Actions Example

Create `.github/workflows/test.yml`:
```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - run: pip install pytest
      - run: pytest test_sorting_algorithms.py -v
```

## Performance Notes

- **QuickSort Recursive**: Fastest on random data, O(n²) on sorted data
- **QuickSort Iterative**: Same complexity, avoids stack overflow
- **MergeSort**: Consistent O(n log n), requires O(n) extra space
- **HeapSort**: Consistent O(n log n), in-place, slower in practice
- **Built-in Sort**: Adaptive Timsort, excellent on real-world data

## Next Steps

1. Run all tests: `pytest test_sorting_algorithms.py -v`
2. Check coverage: `pytest test_sorting_algorithms.py --cov=sorting_algorithms`
3. Profile performance: Add timing to your test runs
4. Extend tests: Add custom test cases as needed

---

**All tests are ready to run! Happy testing!** 🎯
