package org.example.recursion;

public class Sum {

    private static void parameterized(int num, int sum) {
        if (num < 1) {
            System.out.println(sum);
            return;
        }
        parameterized(num - 1, sum + num);
    }

    private static int backTrack(int num) {
        if (num == 1) {
            return 1;
        }

       return num + backTrack(num - 1);
    }

    public static void main(String[] args) {
        // parameterized(3, 0);
        System.out.println(backTrack(4));
    }
}
