import java.util.HashMap;

public class FibonacciDP {
    private static HashMap<Integer, Integer> cache = new HashMap<>();

    public static int fibonacci(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;

        if (cache.containsKey(n)) {
            return cache.get(n);
        }

        int result = fibonacci(n - 1) + fibonacci(n - 2);
        cache.put(n, result);
        return result;
    }

    public static void main(String[] args) {
        int n = 10;
        System.out.println("Fibonacci(" + n + ") = " + fibonacci(n));
    }
}
