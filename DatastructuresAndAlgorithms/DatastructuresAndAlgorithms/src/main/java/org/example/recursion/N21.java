package org.example.recursion;

public class N21 {
    private static void printN21(int n) {
        if (n == 0) {
            return;
        }

        System.out.println(n);
        printN21(n - 1);
    }

    public static void main(String[] args) {
        printN21(5);   
    }
}
