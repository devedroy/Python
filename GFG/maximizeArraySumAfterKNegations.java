import java.util.PriorityQueue;

class maximizeSum {
    public static int maxSum(int[] a, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int x : a) {
            pq.add(x);
        }

        while (k-- > 0) {
            int temp = pq.poll();
            temp *= -1;
            pq.add(temp);
        }
        int sum = 0;
        for (int x : pq) {
            sum += x;
        }
        return sum;
    }

    public static void main(String[] args) {
        int[] a = { -1, -3, -2 };
        int k = 2;
        System.out.println(maxSum(a, k));
    }
}