import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

public class CPUIntervals {
    public static int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> taskCount = new HashMap<>();
        for (char task : tasks) {
            taskCount.put(task, taskCount.getOrDefault(task, 0) + 1);
        }

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        maxHeap.addAll(taskCount.values());

        int intervals = 0;

        while (!maxHeap.isEmpty()) {
            int time = 0;
            List<Integer> temp = new ArrayList<>();

            for (int i = 0; i <= n; i++) {
                if (!maxHeap.isEmpty()) {
                    temp.add(maxHeap.poll());
                    time++;
                }
            }

            for (int count : temp) {
                if (--count > 0) {
                    maxHeap.add(count);
                }
            }

            intervals += maxHeap.isEmpty() ? time : n + 1;
        }

        return intervals;
    }

    public static void main(String[] args) {
        char[] tasks1 = {'A', 'A', 'A', 'B', 'B', 'B'};
        System.out.println(leastInterval(tasks1, 2)); // Output: 8

        char[] tasks2 = {'A', 'C', 'A', 'B', 'D', 'B'};
        System.out.println(leastInterval(tasks2, 1)); // Output: 6

        char[] tasks3 = {'A', 'A', 'A', 'B', 'B', 'B'};
        System.out.println(leastInterval(tasks3, 3)); // Output: 10
    }
}
