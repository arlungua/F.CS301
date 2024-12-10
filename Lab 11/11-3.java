import java.util.HashSet;
import java.util.Set;

class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> deadSet = new HashSet<>();
        for (String dead : deadends) {
            deadSet.add(dead);
        }

        if (deadSet.contains("0000")) {
            return -1;
        }

        Set<String> visited = new HashSet<>();

        int result = dfs("0000", target, deadSet, visited, 0);

        return result == Integer.MAX_VALUE ? -1 : result;
    }

    private int dfs(String current, String target, Set<String> deadSet, Set<String> visited, int steps) {
        if (deadSet.contains(current)) {
            return Integer.MAX_VALUE; // 
        }
        if (visited.contains(current)) {
            return Integer.MAX_VALUE; //
        }
        if (current.equals(target)) {
            return steps; // 
        }

        visited.add(current);

        int minSteps = Integer.MAX_VALUE;

        for (int i = 0; i < 4; i++) {
            char[] currentArray = current.toCharArray();

            currentArray[i] = currentArray[i] == '9' ? '0' : (char) (currentArray[i] + 1);
            String nextForward = new String(currentArray);
            minSteps = Math.min(minSteps, dfs(nextForward, target, deadSet, visited, steps + 1));

            currentArray[i] = currentArray[i] == '0' ? '9' : (char) (currentArray[i] - 2); 
                                                                                           
            String nextBackward = new String(currentArray);
            minSteps = Math.min(minSteps, dfs(nextBackward, target, deadSet, visited, steps + 1));
        }

        visited.remove(current);

        return minSteps;
    }
}
