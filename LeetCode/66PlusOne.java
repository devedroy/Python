class PlusOne {

    public int[] plusOne(int[] digits) {
        int i = digits.length - 1;
        while(true) {
            if(i >= 0) {
                if (digits[i] == 9) {
                    digits[i] = 0;
                } else {
                    digits[i] += 1;
                    break;
                }
            } else {
                return insertElement(0, 1, digits);
            }
            i -= 1;
        }
        return digits;
    }
 
    public static void main(String[] args) {
        int idx = 0, val = 5;
        int[] arr = {1,2, 3};
        int[] result = insertElement(idx, val, arr);
        
        for(int x: result) {
            System.out.println(x);
        }
    }

    private static int[] insertElement(int idx, int val, int[] arr) {
        int newLength = arr.length + 1;
        int[]  newArr = new int[newLength];
        int i = 0, j = 0;
        while (i < newLength) {
            if (i == idx) {
                newArr[i] = val;
            } else {
                newArr[i] = arr[j];
                j += 1;
            }
            i += 1;
        }

        return newArr;
    }
}