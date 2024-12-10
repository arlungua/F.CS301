import java.util.Arrays;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        Arrays.sort(nums);
        return helper(nums, 0, nums.length - 1);
    }

    private TreeNode helper(int[] nums, int left, int right) {
        if (left > right) {
            return null;
        }
        
        int mid = (left + right) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = helper(nums, left, mid - 1);
        root.right = helper(nums, mid + 1, right);
        return root;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {3, 1, 4, 2};  // Unsorted input
        TreeNode bstRoot = solution.sortedArrayToBST(nums);

        printBST(bstRoot);
    }

    private static void printBST(TreeNode node) {
        if (node == null) {
            return;
        }
        printBST(node.left);
        System.out.println(node.val);
        printBST(node.right);
    }
}
