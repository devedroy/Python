import java.util.*;

class LongestSubstringWithoutRepeatingCharacter {


    //naive-approach
    static int longestUniqueSubString(String s) {
        int n = s.length();
        int res = 0;

        for (int i = 0; i < n; i++) {
            boolean[] visited = new boolean[256];
            for (int j = i; j < n; j++) {
                if (visited[s.charAt(j)]) {
                    break;
                } else {
                    res = Math.max(res, j - i + 1);
                    visited[s.charAt(j)] = true;
                }
            }
        }
        return res;
    }

    //sliding_window
    static int longestUniqueSubString_slidingWindow(String str) {

        int res = 0;
        int left = 0, right = 0;
        boolean[] visited = new boolean[256];

        while (right < str.length()) {

            while (visited[str.charAt(right)]) {
                visited[str.charAt(left)] = false;
                left++;
            }

            visited[str.charAt(right)] = true;
            res = Math.max(res, right - left + 1);
            right++;
        }


        return res;
    }

    public static void main(String[] args) {

        String name = "Devpreyo Roy";
        int ans = longestUniqueSubString_slidingWindow(name);
        System.out.println(ans);
    }
}