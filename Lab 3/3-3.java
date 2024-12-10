import java.util.Arrays;

class Solution {
    
    public int[] sortArray(int[] nums) {
        quickSort(nums, 0, nums.length - 1);
        return nums;
    }

    private void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    private int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = (low - 1);
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return i + 1;
    }

    private void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums1 = {5, 2, 3, 1};
        int[] sorted1 = solution.sortArray(nums1);
        System.out.println(Arrays.toString(sorted1)); // Output: [1, 2, 3, 5]

        int[] nums2 = {5, 1, 1, 2, 0, 0};
        int[] sorted2 = solution.sortArray(nums2);
        System.out.println(Arrays.toString(sorted2)); // Output: [0, 0, 1, 1, 2, 5]
    }
}
