# QuickSort Educational Demo

A self-contained web application demonstrating the QuickSort algorithm in JavaScript, with interactive sorting, input validation, and performance benchmarking against the built-in `Array.sort`.

## 🧩 Project Overview
This project is designed for learning and exploration of sorting algorithms. Users can enter a list of numbers, sort them using a hand‑implemented QuickSort, benchmark its performance against the native sort, and run automated tests on randomly generated data.

The entire frontend is built with plain HTML, CSS, and JavaScript – no frameworks or build steps are required. Logic is encapsulated in a modular IIFE to avoid polluting the global scope.

## ✅ Features
- **Pure QuickSort implementation** that returns a new sorted array.
- **In‑place QuickSort** used for benchmarking.
- Comprehensive **input validation** with helpful error messages.
- **Benchmarks** comparing multiple algorithms (QuickSort, MergeSort, HeapSort, BubbleSort) and the built-in sort on sizes 100, 1 000, and 10 000.
- Option to run a parallel QuickSort using a Web Worker.
- Random array generator for fair, repeatable tests.
- Clean UI with separate sections for sorting results and benchmark data.

## 📘 QuickSort Algorithm Explanation
The QuickSort routines use Lomuto partitioning:
1. Choose a pivot (middle element for the pure version; last element for the in-place version).
2. Partition the array into values less than, equal to, and greater than the pivot.
3. Recursively sort the partitions.

Two versions exist:
- `quickSort(arr, low, high)`: mutates the input and is used for speed measurements.
- `quickSortPure(arr)`: returns a new sorted array, preserving the original.

Several bugs (off‑by‑one recursion boundary, mutation leaks) were intentionally introduced during development, then analyzed and corrected, improving robustness and serving as teaching points.

## 📏 Benchmarking Method
Performance is measured using `performance.now()` to obtain high-resolution timestamps. Benchmarks are performed on randomly generated arrays of three sizes. Each size is tested multiple times (default 5 runs) to compute average times.

To ensure fairness:
- Both algorithms receive identical copies of the array.
- Copies are made to avoid mutating the source data.
- DOM updates occur *after* timing so that measurement only reflects algorithm execution.

## 📊 Performance Comparison
The built-in `Array.sort((a, b) => a - b)` is consistently faster due to:
- Engine optimizations (JIT compilation, low-level C/C++ code, cache-friendly operations).
- Use of hybrid algorithms such as Timsort or introsort with worst-case guarantees.
- Avoidance of recursion overhead present in the custom QuickSort.

The custom QuickSort remains useful for education, experimentation, or custom behavior but is not competitive for production sorting needs.

## 🔍 Edge Cases Handled
- Empty input and whitespace-only strings.
- Non‑numeric tokens (e.g. "a" or "1, two, 3") are rejected gracefully.
- Extra commas/spaces and leading/trailing whitespace.
- Handling of empty arrays or arrays with duplicate values.
- Bugs due to recursion boundaries and data mutation were identified and fixed.
- Multiple algorithms correctly handle small/large arrays; bubble sort will still degrade gracefully.

## 🤖 How GitHub Copilot Assisted
Copilot was used extensively to scaffold algorithms, refactor code into modules, craft documentation, and even suggest benchmarking utilities. It helped generate initial versions of QuickSort in multiple languages, then iteratively improved them based on user feedback. Copilot also played a role in creating the final README content and explaining algorithmic decisions.

## 💡 Key Learnings
- Writing and debugging sorting algorithms deepens understanding of recursion and partitioning.
- Input validation is crucial for a smooth UX and to prevent runtime errors.
- Benchmarking reliably requires careful control over data and timing scope.
- Built-in functions are highly optimized and should be preferred unless customization or education is the goal.

## 🚀 Future Improvements
- Add more sophisticated visualizations (e.g. comparison highlights, step controls).
- Support additional algorithms such as Radix sort or TimSort.
- Add UI for selecting whether to run sorting in a Web Worker or main thread.
- Persist benchmark results across sessions using `localStorage` and allow CSV export.
- Provide an interactive API explorer for the REST endpoint.
- Expand tests to include array sizes beyond 10 000 with asynchronous execution to avoid freezing the UI.

---

### 🛠️ Additional Components
- **`worker.js`**: a Web Worker used by the page for parallel QuickSort.
- **`server.js`** (root or in `BONUS`): a minimal Node/Express API exposing `/quicksort`.

The Bonus directory contains a copy of the server plus its own `package.json`. To run the API:

```powershell
cd BONUS
npm install      # install express/body-parser
npm start        # starts server on port 3000 by default
```

You can then POST `{"array":[3,1,2]}` to `http://localhost:3000/quicksort`.

Feel free to open `index.html` in any modern browser and explore the demo interactively.