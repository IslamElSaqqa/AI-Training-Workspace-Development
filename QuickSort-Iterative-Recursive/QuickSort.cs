using System;

class Algorithm
{
    public static void Main(string[] args)
    {
        // Create sample data and display before sorting
        int[] numbers = { 33, 10, 55, 71, 29, 3, 18 };
        Console.WriteLine("Before sorting: " + string.Join(", ", numbers));

        // Perform quick sort on the entire array
        QuickSort(numbers, 0, numbers.Length - 1);

        // Show the results after sorting
        Console.WriteLine("After sorting:  " + string.Join(", ", numbers));
    }

    /// <summary>
    /// Sorts a segment of an integer array in place using the QuickSort algorithm.
    /// </summary>
    /// <param name="array">The array to be sorted.</param>
    /// <param name="low">Starting index of the segment to sort.</param>
    /// <param name="high">Ending index of the segment to sort.</param>
    public static void QuickSort(int[] array, int low, int high)
    {
        // Iterative version with tail recursion elimination to minimize stack usage.
        // Always sort the smaller partition first and loop on the larger one.
        while (low < high)
        {
            // Partition the segment and get pivot position
            int pivotIndex = Partition(array, low, high);

            // Determine which side is smaller
            int leftSize = pivotIndex - 1 - low;
            int rightSize = high - (pivotIndex + 1);

            if (leftSize < rightSize)
            {
                // Recurse on smaller left side
                QuickSort(array, low, pivotIndex - 1);
                // Update bounds to loop on larger right side
                low = pivotIndex + 1;
            }
            else
            {
                // Recurse on smaller right side
                QuickSort(array, pivotIndex + 1, high);
                // Update bounds to loop on larger left side
                high = pivotIndex - 1;
            }
        }
    }

    /// <summary>
    /// Partitions the array segment around a pivot using the Lomuto scheme.
    /// Values <= pivot move to the left; greater values stay on the right.
    /// Choosing the last element as pivot is simple but can degrade on sorted data.
    /// </summary>
    /// <returns>The final index of the pivot.</returns>
    private static int Partition(int[] array, int low, int high)
    {
        int pivot = array[high];      // choose last element as pivot
        int i = low - 1;              // place for swapping

        // Iterate over segment and move smaller values left of pivot
        for (int j = low; j < high; j++)
        {
            if (array[j] <= pivot)
            {
                i++;
                Swap(array, i, j);   // swap current element with i-th position
            }
        }

        // Place pivot after the last smaller element
        Swap(array, i + 1, high);
        return i + 1;
    }

    /// <summary>
    /// Swaps two elements in the given array.
    /// </summary>
    private static void Swap(int[] array, int a, int b)
    {
        int temp = array[a];
        array[a] = array[b];
        array[b] = temp;
    }
}