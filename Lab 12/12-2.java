import java.util.*;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] prereq : prerequisites) {
            graph.get(prereq[0]).add(prereq[1]);
        }
        
        int[] visited = new int[numCourses];
        
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i, visited, graph)) {
                return false; 
            }
        }
        
        return true; 
    }
    
    private boolean dfs(int course, int[] visited, List<List<Integer>> graph) {
        if (visited[course] == 1) {
            return false; 
        }
        if (visited[course] == 2) {
            return true; 
        }
        
        visited[course] = 1;
        for (int prereq : graph.get(course)) {
            if (!dfs(prereq, visited, graph)) {
                return false;
            }
        }
        
        visited[course] = 2;
        return true;
    }
}
