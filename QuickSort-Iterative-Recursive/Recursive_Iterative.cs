using System;

class Recursive_Iterative
{
    // Recursive quicksort (Lomuto partition)
    public static void RecursiveQuickSort(int[] arr, int low, int high)
    {
        if (low < high)
        {
            int pivot = Partition(arr, low, high);
            RecursiveQuickSort(arr, low, pivot - 1);
            RecursiveQuickSort(arr, pivot + 1, high);
        }
    }

    // Iterative quicksort using explicit stack
    public static void IterativeQuickSort(int[] arr)
    {
        int n = arr.Length;
        int[] stack = new int[n];
        int top = -1;

        stack[++top] = 0;
        stack[++top] = n - 1;

        while (top >= 0)
        {
            int high = stack[top--];
            int low = stack[top--];
            if (low < high)
            {
                int pivot = Partition(arr, low, high);
                if (pivot + 1 < high)
                {
                    stack[++top] = pivot + 1;
                    stack[++top] = high;
                }
                if (low < pivot - 1)
                {
                    stack[++top] = low;
                    stack[++top] = pivot - 1;
                }
            }
        }
    }

    private static int Partition(int[] arr, int low, int high)
    {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++)
        {
            if (arr[j] <= pivot)
            {
                i++;
                Swap(arr, i, j);
            }
        }
        Swap(arr, i + 1, high);
        return i + 1;
    }

    private static void Swap(int[] arr, int a, int b)
    {
        int tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
    }

    // optional demonstration
    public static void Main(string[] args)
    {
        int[] data = { 5, 2, 9, 1, 5, 6 };
        Console.WriteLine("Original: " + string.Join(", ", data));
        IterativeQuickSort(data);
        Console.WriteLine("Iterative sorted: " + string.Join(", ", data));
        data = new int[] {5,2,9,1,5,6};
        RecursiveQuickSort(data, 0, data.Length - 1);
        Console.WriteLine("Recursive sorted: " + string.Join(", ", data));
    }
}