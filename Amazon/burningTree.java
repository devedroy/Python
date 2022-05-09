import java.util.Map;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) {
        this.val = val;
    }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public static int search(TreeNode root, int num, Map<Integer> levelOderMap) {
        if (root != null) [
            if (root.val == num) {
                levelOrderStoredInMap(root.left, 1, levelOderMap);
                levelOrderStoredInMap(root.right, 1, levelOderMap);
                return 1;
            }
            int k = search(root.left, num, levelOderMap);

        ]
    }
}