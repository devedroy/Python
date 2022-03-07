class GFG {
    static void memset(int[] arr, int value) {
        for (int i = 0; i < arr.length; i++) {
            arr[i] = value;
        }
    }
    
    static class Node {
        int data;
        Node left, right;
        
    }

    static Node buildCartesianTreeUtil(int root, int arr[], int parent[], int leftChild[], int rightChild[]) {
        if(root == -1) {
            return null;
        }
        Node temp = new Node();
        temp.data = arr[root];
        temp.left = buildCartesianTreeUtil(leftChild[root], arr, parent, leftChild, rightChild);
        temp.right = buildCartesianTreeUtil(rightChild[root], arr, parent, leftChild, rightChild);
        return temp;
    }

    static Node buildCartesianTree (int arr[], int n) {
        int [] parent = new int[n];
        int [] leftChild = new int[n];
        int [] rightChild = new int[n];

        memset(parent, -1);
        memset(leftChild, -1);
        memset(rightChild, -1);

        int root = 0, last;

        for(int i = 1; i <= n - 1; i++) {
            last = i - 1;
            rightChild[i] = -1;

            while(arr[last] <= arr[i] && last != root) {
                last = parent[last];
            }

            if(arr[last] <= arr[i]) {
                parent[root] = i;
                leftChild[i] = root;
                root = i;
            } else if(rightChild[last] == -1) {
                parent[i] = last;
                rightChild[last] = i;
                leftChild[i] = -1;
            } else {
                parent[rightChild[last]] = i;
                leftChild[i] = rightChild[last];
                rightChild[i] = i;
                parent[i] = last;
            }
        }
        parent[root] = -1;

        return (buildCartesianTreeUtil(root, arr, parent, leftChild, rightChild));
    }
    static void printInOrder(Node node) {
        if(node == null) {
            return;
        }
        printInOrder(node.left);
        System.out.print(node.data + " ");
        printInOrder(node.right);
    }
    public static void main(String[] args) {
        int arr[] = {5, 10, 40, 30, 28};
        int n = arr.length;

        Node root = buildCartesianTree(arr, n);
        System.out.println("Inorder traversal of the constructed tree is :");
        printInOrder(root);
    }
}