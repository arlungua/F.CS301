import java.util.*;

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] prereq : prerequisites) {
            graph.get(prereq[1]).add(prereq[0]);
        }

        int[] state = new int[numCourses];
        List<Integer> result = new ArrayList<>();
        boolean[] isPossible = { true };

        for (int course = 0; course < numCourses; course++) {
            if (state[course] == 0) {
                dfs(course, graph, state, result, isPossible);
            }
        }

        if (!isPossible[0])
            return new int[0];
        Collections.reverse(result);
        return result.stream().mapToInt(i -> i).toArray();
    }

    private void dfs(int course, List<List<Integer>> graph, int[] state, List<Integer> result, boolean[] isPossible) {
        if (!isPossible[0])
            return;
        if (state[course] == 1) {
            isPossible[0] = false;
            return;
        }
        if (state[course] == 2)
            return;
        state[course] = 1;
        for (int neighbor : graph.get(course)) {
            dfs(neighbor, graph, state, result, isPossible);
        }
        state[course] = 2;
        result.add(course);
    }
}
