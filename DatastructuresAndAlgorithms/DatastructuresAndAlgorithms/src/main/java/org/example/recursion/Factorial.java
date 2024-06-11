package org.example.recursion;

public class Factorial {

    private static int backTrack(int num) {
        if (num == 1) {
            return 1;
        }

        return num * backTrack(num - 1);
    }
    
    public static void main(String[] args) {
        System.out.println(backTrack(3));
    }
}
