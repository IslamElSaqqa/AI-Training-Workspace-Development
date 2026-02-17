# Sorting Algorithms Comparison

This document compares four major sorting algorithms: **QuickSort**, **MergeSort**, **HeapSort**, and **C# Built-in Array.Sort()**.

---

## Time Complexity

| Algorithm | Best Case | Average Case | Worst Case | Notes |
|-----------|-----------|--------------|-----------|-------|
| **QuickSort** | O(n log n) | O(n log n) | O(n²) | Worst case occurs on sorted/nearly sorted data with poor pivot selection |
| **MergeSort** | O(n log n) | O(n log n) | O(n log n) | Guaranteed consistent performance; divides and merges |
| **HeapSort** | O(n log n) | O(n log n) | O(n log n) | Max-heap construction and extraction |
| **Array.Sort()** (Timsort) | O(n) | O(n log n) | O(n log n) | Hybrid algorithm; O(n) on already sorted data |

---

## Space Complexity

| Algorithm | Space Used | Explanation |
|-----------|-----------|-------------|
| **QuickSort** | O(log n) avg, O(n) worst | Recursion stack: O(log n) balanced, O(n) unbalanced partitions |
| **MergeSort** | O(n) | Requires temporary array for merging |
| **HeapSort** | O(1) | In-place heap operations; no extra arrays |
| **Array.Sort()** (Timsort) | O(n) | Maintains run buffers and temporary storage |

---

## Performance Characteristics

### QuickSort
- **Pros:**
  - Fastest average-case performance
  - Cache-friendly (good locality)
  - In-place sorting with minimal extra space
  - Widely used in practice

- **Cons:**
  - O(n²) worst case (e.g., sorted input with naive pivot)
  - Not stable (may reorder equal elements)
  - Vulnerable to adversarial inputs

### MergeSort
- **Pros:**
  - Guaranteed O(n log n) performance
  - Stable sort (preserves relative order of equal elements)
  - Predictable behavior
  - Parallelizable

- **Cons:**
  - Requires O(n) extra space
  - Slower in practice than QuickSort on average
  - More memory allocations

### HeapSort
- **Pros:**
  - Guaranteed O(n log n) performance
  - O(1) extra space (in-place)
  - No worst-case quadratic behavior
  - Works well with limited memory

- **Cons:**
  - Slower than QuickSort in practice
  - Poor cache locality (random memory access)
  - Not stable
  - Overhead of heap operations

### Array.Sort() (C# Timsort)
- **Pros:**
  - Hybrid algorithm optimized for real-world data
  - O(n) on already sorted runs (adaptive)
  - Excellent practical performance
  - Handles edge cases well
  - Stable sort variant available

- **Cons:**
  - Black-box implementation (hard to customize)
  - Requires O(n) space
  - More complex internally

---

## Stability

| Algorithm | Stable | Notes |
|-----------|--------|-------|
| QuickSort | ❌ No | Swaps may change order of equal elements |
| MergeSort | ✅ Yes | Merging process preserves relative order |
| HeapSort | ❌ No | Heap extraction loses stability |
| Array.Sort() | ✅ Yes (default) | Uses stable Timsort; unstable variant available |

---

## When to Use

### Use **QuickSort** when:
- Average-case performance is prioritized
- Memory is limited (in-place sorting)
- Stability is not required
- Input is random or unsorted

### Use **MergeSort** when:
- Guaranteed O(n log n) performance is needed
- Stability is required
- External sorting is needed
- Parallelization is desired

### Use **HeapSort** when:
- Memory is very constrained (O(1) space)
- Guaranteed performance without O(n) extra space
- Worst-case is a concern

### Use **Array.Sort()** when:
- General-purpose sorting of collections
- Optimal performance on real-world data
- Adapting to pre-sorted runs matters
- Simplicity is prioritized

---

## Benchmark Setup (C#)

The comparison was performed using:
- **Test sizes:** 1,000, 5,000, 10,000, 50,000 elements
- **Test cases:** Random data and pre-sorted data
- **Implementation:** C# with `System.Diagnostics.Stopwatch`
- **Seed:** Fixed seed (42) for reproducible random data

---

## Key Findings

1. **Array.Sort() is fastest overall** due to Timsort's adaptive nature and optimization for common patterns.

2. **QuickSort outperforms HeapSort** in practical scenarios despite similar theoretical complexity.

3. **Pre-sorted data heavily favors Timsort** (O(n)) but hurts QuickSort unless randomized pivot is used.

4. **MergeSort shows consistent O(n log n)** but slower than QuickSort due to merge overhead and allocations.

5. **HeapSort is the slowest** due to poor cache locality and higher constant factors.

---

## Implementation Notes

All implementations use:
- **Lomuto Partition Scheme** (QuickSort)
- **Binary Split** (MergeSort)
- **Max-Heap** (HeapSort)
- **.NET Framework's native sort** (Array.Sort)

---

## Recommendations

| Scenario | Recommended Algorithm |
|----------|----------------------|
| General-purpose sorting | Array.Sort() |
| When stability matters | MergeSort or Array.Sort() |
| Maximum average speed | QuickSort |
| Minimum memory usage | HeapSort |
| Guaranteed O(n log n) | MergeSort or HeapSort |
| Adaptive/pre-sorted data | Array.Sort() or TimSort variant |

---

## References

- **QuickSort:** C.A.R. Hoare, 1960
- **MergeSort:** John von Neumann, 1945
- **HeapSort:** J.W.J. Williams, 1964
- **Timsort:** Tim Peters, 2002