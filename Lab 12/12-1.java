import java.util.*;

class Solution {
    public List<Integer> topologicalSort(int V, int[][] edges) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < V; i++) {
            graph.put(i, new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
        }

        boolean[] visited = new boolean[V];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                dfs(i, visited, stack, graph);
            }
        }

        List<Integer> result = new ArrayList<>();
        while (!stack.isEmpty()) {
            result.add(stack.pop());
        }
        return result;
    }

    private void dfs(int node, boolean[] visited, Stack<Integer> stack, Map<Integer, List<Integer>> graph) {
        visited[node] = true;
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {
                dfs(neighbor, visited, stack, graph);
            }
        }
        stack.push(node);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int V = 6;
        int[][] E = { { 2, 3 }, { 3, 1 }, { 4, 0 }, { 4, 1 }, { 5, 0 }, { 5, 2 } };
        System.out.println(solution.topologicalSort(V, E));
    }
}
