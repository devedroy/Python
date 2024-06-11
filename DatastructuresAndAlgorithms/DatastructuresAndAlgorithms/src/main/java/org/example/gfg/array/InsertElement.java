package org.example.gfg.array;

import java.sql.Array;
import java.util.Arrays;

/**
 * Given
 * arr = {2,4,3,6,_,_}
 * size = 4
 * capacity = 6
 * todo -> insert 1 at position 2
 * Expected
 * arr = {2,1,4,3,6,_}
 * size = 5
 */

public class InsertElement {
    private static int[] insertElement(int[] arr, int size, int position, int value, int capacity) {
        if (capacity <= size) {
            return arr;
        } else {
            //6-4-1 = 1
            int end = capacity - size - 1;
            for (int i = end - 1; i >= 0; i--) {
                arr[i] = arr[i - 1];
            }
            arr[position - 1] = value;
        }
        return arr;
    }

    public static void main(String[] args) {
        int[] arr = {2, 4, 3, 6, -1, -1};
        int size = 4;
        int capacity = arr.length;
        int position = 2;
        int value = 1;

        System.out.print(Arrays.toString(insertElement(arr, size, position, value, capacity)));


    }
}
