import java.io.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public class Solution {
    public static int minimumSwap(List<Integer> nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int swaps = 0;

        for (int i = 0; i < nums.size(); i++) {
            map.put(nums.get(i), i);
        }

        for (int i = 0; i < nums.size(); i++) {
            int target = i+1;
            int targetPosition = map.get(target);
            int currentValue = nums.get(i);

            if (targetPosition != i) {
                nums.set(targetPosition, currentValue);
                map.put(currentValue, targetPosition);
                swaps++;
            }
        }

        return swaps;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        bufferedReader.readLine();
        List<Integer> nums = Arrays.stream(bufferedReader.readLine().split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toList());

        bufferedWriter.write(String.valueOf(minimumSwap(nums)));

        bufferedReader.close();
        bufferedWriter.close();
    }
}
