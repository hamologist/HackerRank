import java.io.*;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Query {
    final private int a;
    final private int b;
    final private int k;

    public Query(int a, int b, int k) {
        this.a = a;
        this.b = b;
        this.k = k;
    }

    public int getA() {
        return a;
    }

    public int getB() {
        return b;
    }

    public int getK() {
        return k;
    }
}

public class Solution {
    public static long arrayManipulation(int n, List<Query> queries) {
        long[] nums = new long[n + 1];

        for (Query query: queries) {
            int k = query.getK();
            nums[query.getA() - 1] += k;
            nums[query.getB()] -= k;
        }

        long sum = 0;
        long largestValue = 0;
        for (long num: nums) {
            sum += num;
            largestValue = Math.max(sum, largestValue);
        }

        return largestValue;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        List<Integer> pairs = Arrays.stream(bufferedReader.readLine().split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toList());
        int n = pairs.get(0);
        List<Query> queries = bufferedReader.lines()
                .map(l -> Arrays.stream(l.split(" "))
                        .map(Integer::parseInt)
                        .collect(Collectors.toList()))
                .map(l -> new Query(l.get(0), l.get(1), l.get(2)))
                .collect(Collectors.toList());

        bufferedWriter.write(String.valueOf(arrayManipulation(n, queries)));

        bufferedReader.close();
        bufferedWriter.close();
    }
}
