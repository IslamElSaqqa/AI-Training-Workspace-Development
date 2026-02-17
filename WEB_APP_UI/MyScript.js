// QuickDemo module encapsulates all logic to avoid global scope pollution
const QuickDemo = (function () {
    /**
     * Parse comma/space-separated string into number array.
     * @param {string} str
     * @returns {number[]|null} null on invalid input
     */
    function parseNumbers(str) {
        // trim whitespace so " 1 , 2" doesn't produce empty tokens and
        // leading/trailing spaces aren't treated as data
        str = str.trim();
        if (!str) {
            return null;
        }
        const parts = str.split(/[\s,]+/).filter(p => p !== '');
        if (parts.length === 0) {
            return null;
        }
        const nums = [];
        for (let p of parts) {
            const n = Number(p);
            if (isNaN(n)) {
                // non-numeric token found
                return null;
            }
            nums.push(n);
        }
        return nums;
    }

    // standard recursive QuickSort using Lomuto partition – mutates array in place
    // standard recursive QuickSort using Lomuto partition – mutates array in place
    // note: earlier a logical bug (recurse on [pi,high] instead of [pi+1,high]) could cause
    // infinite recursion when pivot ended up at 'low' or duplicates existed. Always ensure
    // the right-hand call starts one past the partition index.
    function quickSort(arr, low = 0, high = arr.length - 1) {
        if (low < high) {
            const pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high); // fixed boundary
        }
    }

    /**
     * Pure recursive QuickSort that returns a new sorted array without mutating input.
     * Uses divide-and-conquer with pivot chosen from middle element for stability
     * on already sorted data. Handles empty, single-element, duplicates, negatives.
     *
     * @param {number[]} arr - array to sort
     * @returns {number[]} sorted copy of arr
     */
    function quickSortPure(arr) {
        if (arr.length <= 1) {
            return arr.slice(); // return shallow copy
        }
        const pivot = arr[Math.floor(arr.length / 2)];
        const less = [];
        const equal = [];
        const greater = [];
        for (let x of arr) {
            if (x < pivot) {
                less.push(x);
            } else if (x > pivot) {
                greater.push(x);
            } else {
                equal.push(x);
            }
        }
        return quickSortPure(less).concat(equal).concat(quickSortPure(greater));
    }

    // MergeSort (pure, returns new array)
    function mergeSort(arr) {
        if (arr.length <= 1) return arr.slice();
        const mid = Math.floor(arr.length / 2);
        const left = mergeSort(arr.slice(0, mid));
        const right = mergeSort(arr.slice(mid));
        return merge(left, right);
    }

    function merge(left, right) {
        const res = [];
        let i = 0, j = 0;
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) res.push(left[i++]);
            else res.push(right[j++]);
        }
        return res.concat(left.slice(i)).concat(right.slice(j));
    }

    // HeapSort (in-place)
    function heapSort(arr) {
        const n = arr.length;
        for (let i = Math.floor(n/2)-1; i >= 0; i--) heapify(arr, n, i);
        for (let i = n-1; i > 0; i--) {
            [arr[0], arr[i]] = [arr[i], arr[0]];
            heapify(arr, i, 0);
        }
    }

    function heapify(arr, n, i) {
        let largest = i;
        const l = 2*i + 1;
        const r = 2*i + 2;
        if (l < n && arr[l] > arr[largest]) largest = l;
        if (r < n && arr[r] > arr[largest]) largest = r;
        if (largest !== i) {
            [arr[i], arr[largest]] = [arr[largest], arr[i]];
            heapify(arr, n, largest);
        }
    }

    // BubbleSort (in-place)
    function bubbleSort(arr) {
        const n = arr.length;
        for (let i = 0; i < n-1; i++) {
            for (let j = 0; j < n-1-i; j++) {
                if (arr[j] > arr[j+1]) {
                    [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
                }
            }
        }
    }

    // Visualization support: record swap steps
    function recordMergeSortSteps(arr, steps) {
        if (arr.length <= 1) return arr.slice();
        const mid = Math.floor(arr.length / 2);
        const left = recordMergeSortSteps(arr.slice(0, mid), steps);
        const right = recordMergeSortSteps(arr.slice(mid), steps);
        const merged = [];
        let i = 0, j = 0;
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) merged.push(left[i++]);
            else merged.push(right[j++]);
        }
        return merged.concat(left.slice(i)).concat(right.slice(j));
    }

    function recordQuickSortSteps(arr, low=0, high=arr.length-1, steps) {
        if (low < high) {
            const pi = partition(arr, low, high, steps);
            recordQuickSortSteps(arr, low, pi-1, steps);
            recordQuickSortSteps(arr, pi+1, high, steps);
        }
    }

    function partition(arr, low, high, steps) {
        const pivot = arr[high];
        let i = low -1;
        for (let j=low;j<high;j++){
            if (arr[j] <= pivot) {
                i++;
                [arr[i], arr[j]] = [arr[j], arr[i]];
                if (steps) steps.push({type:'swap', i, j});
            }
        }
        [arr[i+1], arr[high]] = [arr[high], arr[i+1]];
        if (steps) steps.push({type:'swap', i: i+1, j: high});
        return i+1;
    }

    // similar step recording could be added for other algorithms if needed

    function visualizeSteps(arr) {
        const canvas = document.getElementById('viz');
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0,0,canvas.width,canvas.height);
        const n = arr.length;
        const barWidth = canvas.width / n;
        function draw(array) {
            ctx.clearRect(0,0,canvas.width,canvas.height);
            for(let i=0;i<n;i++){
                const h = (canvas.height * array[i]) / Math.max(...array);
                ctx.fillRect(i*barWidth, canvas.height - h, barWidth, h);
            }
        }
        const steps = [];
        const working = arr.slice();
        recordQuickSortSteps(working,0,working.length-1,steps);
        // animate
        let idx =0;
        function step() {
            if (idx < steps.length) {
                const s = steps[idx++];
                if (s.type==='swap') {
                    [working[s.i], working[s.j]] = [working[s.j], working[s.i]];
                }
                draw(working);
                requestAnimationFrame(step);
            }
        }
        draw(arr);
        step();
    }

    // parallel quicksort using Web Worker
    let worker;
    function initWorker() {
        if (window.Worker) {
            worker = new Worker('worker.js');
            worker.onmessage = function(e){
                const sorted = e.data;
                document.getElementById('output').textContent = 'Parallel QuickSort result: ' + JSON.stringify(sorted);
            };
        }
    }


    function partition(arr, low, high) {
        const pivot = arr[high];
        let i = low - 1;
        for (let j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                [arr[i], arr[j]] = [arr[j], arr[i]];
            }
        }
        [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
        return i + 1;
    }

    // measure performance of QuickSort vs built-in sort on a provided array
    // returns timing data but does not output anything to the page (DOM is updated by callers)
    function benchmark(arr) {
        const original = arr.slice();
        const result = {};

        let copy = original.slice();
        let t0 = performance.now();
        quickSort(copy);
        let t1 = performance.now();
        result.quick = { time: t1 - t0, sorted: copy.slice() };

        copy = original.slice();
        t0 = performance.now();
        copy.sort((a, b) => a - b);
        t1 = performance.now();
        result.builtin = { time: t1 - t0, sorted: copy.slice() };

        return result;
    }

    // helper to generate an array of the given size filled with random numbers
    function generateRandomArray(size) {
        const arr = new Array(size);
        for (let i = 0; i < size; i++) {
            // random integer between 0 and 999999
            arr[i] = Math.floor(Math.random() * 1000000);
        }
        return arr;
    }

    // run single benchmark on one array, return quick/builtin times
    function runOneBenchmark(arr) {
        const original = arr.slice();
        // always copy when timing so both algorithms get identical unsorted input
        const copy1 = original.slice();
        const t0 = performance.now();
        quickSort(copy1);
        const t1 = performance.now();
        const quick = t1 - t0;

        const copy2 = original.slice();
        const t2 = performance.now();
        copy2.sort((a, b) => a - b);
        const t3 = performance.now();
        const builtin = t3 - t2;

        return { quick, builtin };
    }

    // run multiple iterations for a given size and return average times
    function avgBenchmark(size, runs = 5) {
        let sumQuick = 0;
        let sumBuilt = 0;
        for (let i = 0; i < runs; i++) {
            const arr = generateRandomArray(size);
            const res = runOneBenchmark(arr);
            sumQuick += res.quick;
            sumBuilt += res.builtin;
        }
        return { quick: sumQuick / runs, builtin: sumBuilt / runs };
    }

    // driver for full benchmarks (100, 1000, 10000) and display output
    function runFullBenchmark() {
        const sizes = [100, 1000, 10000];
        const results = [];
        const runs = 5;
        for (let size of sizes) {
            const avg = avgBenchmark(size, runs);
            results.push({ size, avg });
        }
        displayFullBenchmark(results);
    }

    function displayFullBenchmark(results) {
        const div = document.getElementById('fullBenchmark');
        let text = 'Size\tQuickSort(ms)\tBuilt-in(ms)\n';
        for (let r of results) {
            text += `${r.size}\t${r.avg.quick.toFixed(3)}\t${r.avg.builtin.toFixed(3)}\n`;
        }
        div.textContent = text;
    }

    // click handler separated for clarity
    function handleSort() {
        const raw = document.getElementById('numbers').value;
        const input = raw.trim();
        const errDiv = document.getElementById('error');
        const outDiv = document.getElementById('output');
        errDiv.textContent = '';
        outDiv.textContent = '';

        if (!input) {
            errDiv.textContent = 'Please provide one or more numbers to sort.';
            return;
        }
        const nums = parseNumbers(input);
        if (nums === null) {
            errDiv.textContent = 'Invalid input. Make sure you enter only numbers separated by commas or spaces.';
            return;
        }
        if (nums.length === 0) {
            outDiv.textContent = '[]';
            return;
        }
        const algo = document.getElementById('algorithm').value;
        let result;
        switch(algo) {
            case 'merge':
                result = mergeSort(nums);
                break;
            case 'heap':
                const heapArr = nums.slice();
                heapSort(heapArr);
                result = heapArr;
                break;
            case 'bubble':
                const bubArr = nums.slice();
                bubbleSort(bubArr);
                result = bubArr;
                break;
            case 'parallel':
                if (!worker) initWorker();
                worker.postMessage(nums);
                return; // output will be handled by worker
            case 'quick':
            default:
                result = quickSortPure(nums);
        }
        outDiv.textContent = `${algo[0].toUpperCase()+algo.slice(1)} result: ` + JSON.stringify(result);
    }

    function handleBenchmark() {
        const raw = document.getElementById('numbers').value;
        const input = raw.trim();
        const errDiv = document.getElementById('error');
        const benchDiv = document.getElementById('benchmark');
        errDiv.textContent = '';
        benchDiv.textContent = '';

        if (!input) {
            errDiv.textContent = 'Please provide some numbers to benchmark.';
            return;
        }

        const nums = parseNumbers(input);
        if (nums === null) {
            errDiv.textContent = 'Invalid input. Make sure you enter only numbers separated by commas or spaces.';
            return;
        }

        if (nums.length === 0) {
            benchDiv.textContent = '[]';
            return;
        }
        const algo = document.getElementById('algorithm').value;
        let quickTime;
        if (algo === 'merge') {
            const copy = nums.slice();
            const t0 = performance.now();
            mergeSort(copy);
            const t1 = performance.now();
            quickTime = t1 - t0;
        } else if (algo === 'heap') {
            const copy = nums.slice();
            const t0 = performance.now();
            heapSort(copy);
            const t1 = performance.now();
            quickTime = t1 - t0;
        } else if (algo === 'bubble') {
            const copy = nums.slice();
            const t0 = performance.now();
            bubbleSort(copy);
            const t1 = performance.now();
            quickTime = t1 - t0;
        } else {
            const copy = nums.slice();
            const t0 = performance.now();
            quickSort(copy);
            const t1 = performance.now();
            quickTime = t1 - t0;
        }
        const copy2 = nums.slice();
        const t2 = performance.now();
        copy2.sort((a, b) => a - b);
        const t3 = performance.now();
        const builtinTime = t3 - t2;
        benchDiv.textContent =
            `${algo} time: ${quickTime.toFixed(3)} ms\n` +
            `built-in sort time: ${builtinTime.toFixed(3)} ms`;
    }

    function init() {
        document.getElementById('sortBtn').addEventListener('click', handleSort);
        document.getElementById('benchmarkBtn').addEventListener('click', handleBenchmark);
        const fullBtn = document.getElementById('fullBenchBtn');
        if (fullBtn) {
            fullBtn.addEventListener('click', runFullBenchmark);
        }
        const visBtn = document.getElementById('visualizeBtn');
        if (visBtn) {
            visBtn.addEventListener('click', () => {
                const raw = document.getElementById('numbers').value.trim();
                const nums = parseNumbers(raw);
                if (nums && nums.length > 0) visualizeSteps(nums);
            });
        }
        initWorker();
    }

    // public API
    return {
        init: init
    };
})();

// initialize when document ready
document.addEventListener('DOMContentLoaded', QuickDemo.init);