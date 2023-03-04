public class Even {
    public static void main(String[] args) {
        System.out.println("Even numbers between 1 and 100 are:");
        
        for (int i = 1; i <= 100; i++) {
           if (i % 2 == 0) {
               System.out.println(i);
           }
       }
       
    }
}