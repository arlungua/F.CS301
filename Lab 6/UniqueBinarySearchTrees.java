public class UniqueBinarySearchTrees {
    public int numTrees(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 1; 
        dp[1] = 1; 

        for (int nodes = 2; nodes <= n; nodes++) {
            for (int i = 1; i <= nodes; i++) {
                dp[nodes] += dp[i - 1] * dp[nodes - i];
            }
        }

        return dp[n];
    }

    public static void main(String[] args) {
        UniqueBinarySearchTrees solution = new UniqueBinarySearchTrees();
        
        int n1 = 3;
        System.out.println("Input: n = " + n1 + "\nOutput: " + solution.numTrees(n1)); // Output: 5
 
        int n2 = 1;
        System.out.println("Input: n = " + n2 + "\nOutput: " + solution.numTrees(n2)); // Output: 1
    }
}
