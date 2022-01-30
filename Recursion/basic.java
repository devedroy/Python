class Test {
    
    static void func1() {
        System.out.println("func1");
    } 

    static void func2() {
        System.out.println(" Before func1");
        func1();
        System.out.println(" After func1");
    }
    public static void main(String[] args) {
        
        System.out.println("Before func2");
        func2();
        System.out.println("After func2");
    }
}