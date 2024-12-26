package org.example.leetcode.array;


public class SearchInsert {

    private static int getIndex(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        int mid = left + (right - left) / 2;
        while (left <= right) {
            mid = left + (right - left) / 2;
            if (arr[mid] == target) {
               break;
            }
            if (arr[mid] < target) {
                left = mid + 1;
            }
            if (arr[mid] > target) {
                right = mid - 1;
            }
        }
        return mid;
    }

    public static int searchInsert(int[] nums, int target) {
        int i;
        for (i = 0; i < nums.length; i++) {
            if (nums[i] >= target) {
                break;
            }
        }
        return i;
    }

    public static void main(String[] args) {

        int[] nums = {1, 3, 5, 6};

//        int target = 5;
        int target = 2;
//        int target = 7;

        System.out.println(getIndex(nums, target));

    }
}
