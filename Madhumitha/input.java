import java.util.Scanner;

class Input{

    public static int search(int[] intArray, int search){
        for(int i = 0; i < intArray.length; i++){
            if(intArray[i] == search){
                return i;
            }
        }
        return -1;
    }


    public static void main(String[] args) {
        // Scanner sc = new Scanner(System.in);
        // System.out.println("Enter a number");
        // int var = sc.nextInt();
        // System.out.println("You entered: " + var);
      

        int intArray2[] = new int[10];

        //homogeneous data
        //collection data
        //starts from 0
        //ends at length-1
        //length = 10 -> 0 to 9

        //Array Operations
        //1. Searching elements
        //2. Inserting elements
        //3. Deleting elements
        //4. Sorting elements

        
        int intArray[] = new int[]{1,2,3,4,5,6,7,8,9,10};
        System.out.println(intArray[0]);
        for(int index = 0; index < intArray.length; index++){
            System.out.println(intArray[index]);
        }

        int search = 5;

        int index = search(intArray, search);
        System.out.println("Index of " + search + " is " + index);

    }
}