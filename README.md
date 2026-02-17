# QuickSort Recursive vs Iterative

This repository contains two implementations of the QuickSort algorithm in Java:

- `recursiveSort`: classic recursive version
- `iterativeSort`: uses an explicit stack to eliminate recursion

## Time Complexity

| Version     | Average Case | Worst Case |
|-------------|--------------|------------|
| Recursive   | O(n log n)   | O(n^2)     |
| Iterative   | O(n log n)   | O(n^2)     |

Both algorithms partition the array and process subarrays. The iterative variant removes recursion, but does not change the time complexity.

## Space Complexity

| Version     | Additional Space | Explanation |
|-------------|------------------|-------------|
| Recursive   | O(log n) average, O(n) worst-case | recursion stack depth proportional to height of recursion tree; worst-case unbalanced partitions.
| Iterative   | O(log n) average, O(n) worst-case | explicit stack used to store subarray bounds; same behaviour as recursion space but in the heap rather than call stack.

The recursive implementation may encounter a `StackOverflowError` on very deep recursion. The iterative version avoids that by managing its own stack.

## Notes

- Both versions are in-place and require only constant extra memory for swaps.
- Pivot selection strategy (last element) can degrade performance on sorted or nearly sorted data.

## Unit Tests

JUnit tests (`QuickSortTest.java`) verify correct sorting for edge cases and compare outputs of the two implementations.

To run the tests, add JUnit 5 to the classpath and use `mvn test` or similar tooling.