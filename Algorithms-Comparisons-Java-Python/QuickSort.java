// QuickSort.java
// Implements both recursive and iterative versions of quicksort for integer arrays.

public class QuickSort {
    /**
     * Recursive quicksort implementation using Lomuto partition scheme.
     */
    public static void recursiveSort(int[] arr, int low, int high) {
        if (low < high) {
            int pivot = partition(arr, low, high);
            recursiveSort(arr, low, pivot - 1);
            recursiveSort(arr, pivot + 1, high);
        }
    }

    /**
     * Iterative quicksort using an explicit stack to eliminate recursion.
     */
    public static void iterativeSort(int[] arr) {
        int n = arr.length;
        // stack for low/high indices
        int[] stack = new int[n];
        int top = -1;

        // push initial boundaries
        stack[++top] = 0;
        stack[++top] = n - 1;

        while (top >= 0) {
            int high = stack[top--];
            int low = stack[top--];

            if (low < high) {
                int pivot = partition(arr, low, high);
                // push right side
                if (pivot + 1 < high) {
                    stack[++top] = pivot + 1;
                    stack[++top] = high;
                }
                // push left side
                if (low < pivot - 1) {
                    stack[++top] = low;
                    stack[++top] = pivot - 1;
                }
            }
        }
    }

    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return i + 1;
    }

    private static void swap(int[] arr, int a, int b) {
        int tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
    }

    // simple utility main for manual testing
    public static void main(String[] args) {
        int[] data = {3,5,1,6,4,2};
        System.out.println("Before: ");
        for (int x : data) System.out.print(x + " ");
        System.out.println();
        recursiveSort(data, 0, data.length - 1);
        System.out.println("After recursive: ");
        for (int x : data) System.out.print(x + " ");
        System.out.println();
    }
}