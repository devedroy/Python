public class isPallindromeString {

    static boolean isPalRec(String str, int start, int end) {
        if (start == end) {
            return true;
        }

        if ((str.charAt(start) != str.charAt(end))) {
            return false;
        }

        if (start < end + 1) {
            return isPalRec(str, start + 1, end - 1);
        }

        return true;
    }

    static boolean isPallindrome(String str) {

        int n = str.length();

        if (n == 0) {
            return true;
        }
        return isPalRec(str, 0, n - 1);
    }
    public static void main(String[] args) {
        String str = "madam";
        if (isPallindrome(str)) {
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }
    }
}
