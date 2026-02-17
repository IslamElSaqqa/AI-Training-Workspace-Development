# QuickSort Implementation Explanation

This document describes the C# implementation of the QuickSort algorithm contained in `Algorithm.cs`.

## Overview

- Algorithm type: **In-place, comparison-based sort**.
- Uses **divide-and-conquer** via partitioning around a pivot.
- Optimized to reduce recursion depth and stack usage.

## `Main` Method

- Sets up sample integer array.
- Prints array before and after sorting.
- Calls `QuickSort` with full range indices.

```csharp
int[] numbers = { 33, 10, 55, 71, 29, 3, 18 };
QuickSort(numbers, 0, numbers.Length - 1);
```

## `QuickSort` Method

Signature:

```csharp
public static void QuickSort(int[] array, int low, int high)
```

### Purpose
Recursively (and iteratively) sort the segment from `low` to `high`.

### Key features

1. **Tail recursion elimination** – executed by looping on the larger subarray and recursing only on the smaller one. This lowers the maximum call stack depth to `O(log n)` in the average case.
2. **While loop** – replaces one of the recursive calls, converting the recursion into iteration.
3. **Size comparison** – determine which partition (left or right of pivot) is smaller to decide recursion target.

### Workflow

1. Call `Partition` to position pivot correctly.
2. Compute sizes of left and right partitions.
3. Recurse on smaller partition.
4. Adjust `low`/`high` to iterate through remaining portion.

## `Partition` Method

Signature:

```csharp
private static int Partition(int[] array, int low, int high)
```

### Purpose
Rearrange elements between `low` and `high` so that all values less than or equal to the pivot end up left of it, with greater values on the right.

### Details
- Uses the **Lomuto partition scheme**.
- Chooses the **last element** as pivot (simple but worst-case on sorted input).
- Iterates once through the segment, performing swaps when elements are <= pivot.
- After loop, places pivot immediately after the last smaller element and returns its index.

## `Swap` Utility

```csharp
private static void Swap(int[] array, int a, int b)
```

Performs a simple three-way value swap of indices `a` and `b`.

## Performance and Memory Optimizations

- **Stack depth reduction**: reducing recursion by always sorting the smaller portion first and looping on the larger keeps stack usage `O(log n)` in average/expected cases.
- **In-place sorting**: uses constant extra space aside from recursion stack.
- **Pivot choice note**: current implementation picks last element; performance can degrade to `O(n^2)` for already sorted arrays. Using median-of-three or random pivot improves reliability.

## Potential Enhancements

- Convert fully to an iterative algorithm using an explicit stack or manual loop.
- Use randomized pivot or median-of-three to avoid worst-case inputs.
- Extend to generic types using `IComparable`.

---

This explanation should help maintainers understand how the code works and identify where further optimizations or features can be added.