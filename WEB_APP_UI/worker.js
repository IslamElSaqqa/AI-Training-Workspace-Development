// Web Worker performing QuickSort in a separate thread
self.onmessage = function(e) {
    const arr = e.data;
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
    function quickSort(arr, low = 0, high = arr.length - 1) {
        if (low < high) {
            const pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }
    const copy = arr.slice();
    quickSort(copy);
    self.postMessage(copy);
};