public class AggregateAnalysis {
    public static void main(String[] args) {
        int n = 10; 
        int totalCost = 0; 
        int logValue = 1; 

        for (int i = 1; i <= n; i++) {
            if (i == logValue) {
                totalCost += i; 
                logValue *= 2;
            } else {
                totalCost += 1; 
            }
        }

        System.out.println("Total cost for " + n + " operations: " + totalCost);

        double amortizedCost = (double) totalCost / n;
        System.out.println("Amortized cost per operation: " + amortizedCost);
    }
}
