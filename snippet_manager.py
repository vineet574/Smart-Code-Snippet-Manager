import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Enable debug print statements
        boolean showOperations = true;

        int T = sc.nextInt(); // number of test cases
        while (T-- > 0) {
            int n = sc.nextInt(), k = sc.nextInt();
            Set<Integer> seen = new HashSet<>();
            Deque<Integer> dq = new ArrayDeque<>();

            System.out.println("Processing " + n + " elements, capacity = " + k);

            for (int i = 0; i < n; i++) {
                int x = sc.nextInt();
                if (seen.contains(x)) {
                    if (showOperations) System.out.println("Skip duplicate: " + x);
                    continue;
                }
                if (dq.size() == k) {
                    int removed = dq.removeLast();
                    seen.remove(removed);
                    if (showOperations) System.out.println("Removed oldest: " + removed);
                }
                dq.addFirst(x);
                seen.add(x);
                if (showOperations) System.out.println("Inserted: " + x);
            }

            System.out.println("Final size: " + dq.size());
            System.out.print("Final elements (latest to oldest): ");
            dq.forEach(e -> System.out.print(e + " "));
            System.out.println();

            System.out.print("Final elements (original insertion order): ");
            List<Integer> originalOrder = new ArrayList<>(dq);
            Collections.reverse(originalOrder);
            originalOrder.forEach(e -> System.out.print(e + " "));
            System.out.println("\n---");
        }
    }
}
