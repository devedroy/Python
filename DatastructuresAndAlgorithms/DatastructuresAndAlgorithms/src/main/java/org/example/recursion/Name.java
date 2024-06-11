package org.example.recursion;

public class Name {

    private static void printName(int n){
        if (n == 0) {
            return;
        }
        System.out.println("Name");
        printName(n - 1);
    }

    public static void main(String[] args) {
        printName(5);
    }
    
}
