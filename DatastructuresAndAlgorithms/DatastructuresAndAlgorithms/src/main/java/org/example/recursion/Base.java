package org.example.recursion;

public class Base {

    private static int count = 0;
    private static void fun() {
        if (count == 3) {
            return;
        }
        System.out.println(count);
        count++;
        fun();
    }

    public static void main(String[] args) {
        fun();
    }
    
}
