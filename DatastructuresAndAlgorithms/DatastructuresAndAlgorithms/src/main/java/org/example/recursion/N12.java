package org.example.recursion;

public class N12 {
    private static int curr = 1;

    private static void print12N(int n) {
        if (curr > n) {
            return;
        }

        System.out.println(curr);
        curr++;
        print12N(n);
    }

    private static void printWithoutGlobal(int curr, int n) {
        if (curr > n) {
            return;
        }
        System.out.println(curr);
        printWithoutGlobal(curr + 1, n);
    }

    private static void backTrack(int n) {
        if (n < 1) {
            return;
        }
        backTrack(n - 1);
        System.out.println(n);
    }

    public static void main(String[] args) {
        // print12N(5);
        // printWithoutGlobal(2, 5);
        backTrack(5);
    }
    
}
