public class SSST {

    public static void main(String[] args) {
        int AB = 30, BC = 40, CA = 60;

        if((AB + BC) > CA && (AB + CA) > BC && (BC + CA) > AB) {
            System.out.println("The three sides can form a triangle");
        }
        else {
            System.out.println("The three sides cannot form a triangle");
        }
    }
  
}
