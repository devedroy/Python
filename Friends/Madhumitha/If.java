import java.util.Scanner;

public class If {

    // if
    //if else
    //else if
    //switch

    //0 1;False, True

    public static void main(String[] args) {

        int income;

        System.out.println("Enter Your Income: ");
        
        Scanner scanner = new Scanner(System.in); 
        income = scanner.nextInt();
        

        if(income <= 100000) {
            System.out.println("Madhumitha "+ income);
        }

        if (income <= 600000 && income > 100000) {
            System.out.println("Madhu's Dad "+ income);
        }
    }
}
