package org.example.tree;

public class BinaryTree {

    private static TreeNode deleteLeafNodes(TreeNode root) {
        if (root == null) return null;
        if (root.left == null && root.right == null) {
            return null;
        }

        root.left = deleteLeafNodes(root.left);
        root.right = deleteLeafNodes(root.right);

        return root;
    }

    private static TreeNode deleteLeafNodesTarget(TreeNode root, int target) {
        if (root == null) return null;
        if (root.left == null && root.right == null && root.val == target) {
            return null;
        }

        root.left = deleteLeafNodes(root.left);
        root.right = deleteLeafNodes(root.right);

        return root;
    }

    private static void inOrderTraversal(TreeNode root) {
        if (root == null) return;
        inOrderTraversal(root.left);
        System.out.print(root.val + " ");
        inOrderTraversal(root.right);
    }

    public static void main(String[] args) {
        TreeNode tree = new TreeNode(1);
        tree.left = new TreeNode(2);
        tree.right = new TreeNode(3);
        tree.left.left = new TreeNode(4);
        tree.left.right = new TreeNode(5);
        tree.right.right = new TreeNode(6);
        tree.left.left.left = new TreeNode(7);
        tree.right.right.right = new TreeNode(8);

        deleteLeafNodes(tree);

        inOrderTraversal(tree);
    }
}
