class SubarraySumEqualsK {
    public static void main(String[] args) {
        int[] arr = {1,1,1};
        //new int[size];
        int k = 1;

        int result = subarraySum(arr,k);
        System.out.println(result);
    }

    private static int subarraySum(int[] arr, int k) {
        int res = 0;
        
        for(int i = 0;i < arr.length;i++) {
            int tempSum = 0;
            for (int j = i; j < arr.length;j++) {
                tempSum += arr[j];
                if (tempSum == k) {
                    res += 1;
                }
            }
        }
        return res;
    }
}