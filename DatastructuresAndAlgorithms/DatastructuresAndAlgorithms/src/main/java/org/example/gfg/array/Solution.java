package org.example.gfg.array;

public class Solution {
    private static int[] removeDuplicates(int[] nums) {
        int counter = 0;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                counter++;
            } else {
                nums[i - 1] = -1;
            }
        }

        int[] result = new int[counter];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != -1) {
                result[counter++] = nums[i];
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int[] result = removeDuplicates(new int[]{1, 1, 2, 2});

        for (int item : result) {
            System.out.println(item);
        }
    }
}
