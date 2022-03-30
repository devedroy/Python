public class EvenIncrease2N {
    /*
    0
    22
    444
    6666
    88888


    0
    24
    6810
    12141618
    2022242628
    */
    public static void main(String[] args) {
        int p = 0;
        for(int i = 0; i < 5;) {
            for(int j = 0; j <= i; j++, p+=2) {
                System.out.print(p);
            }
            i++;
            System.out.println();
        }
    }
}