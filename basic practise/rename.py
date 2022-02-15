# // class Solution {
    
# //     public static void main (String[] args) {
# //         String inp = "Bangalore is in India";
        
# //         int lengnth = inp.length();
        
# //         for (int i = 0; lengnth; i ++ ) {
# //             if (inp[i] == 'n' || inp[i] == 'N') {
# //                 inp[i] = "";
# //             }

# //         }
# //         System.out.println(inp);
# //     }
string = "Bangalore is in India"

n = string.replace("n", "")
N = n.replace("N", "")
print(N)