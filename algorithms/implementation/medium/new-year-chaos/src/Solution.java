import java.io.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public class Solution {

    public static void minimumBribe(List<Integer> nums) {
        int bribes = 0;
        boolean chaotic = false;
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.size(); i++) {
            map.put(nums.get(i), i);
        }

        for (int i = map.size() - 1; i >= 0; i--) {
            int expected = i + 1;
            int position = map.get(expected);

            if (position < i) {
                int moves = i - position;

                if (moves > 2) {
                    chaotic = true;
                    break;
                }

                for (int j = 1; j <= moves; j++) {
                    int whoWasCut = nums.get(position + j);
                    int previousPosition = position + j - 1;

                    nums.set(previousPosition, whoWasCut);
                    map.put(whoWasCut, previousPosition);
                }
                nums.set(position + moves, expected);
                map.put(expected, position + moves);

                bribes += moves;
            }
        }

        if (chaotic) {
            System.out.println("Too chaotic");
        } else {
            System.out.println(bribes);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int numOfTestCases = Integer.parseInt(bufferedReader.readLine());
        for (int i = 0; i < numOfTestCases; i++) {
            bufferedReader.readLine();
            List<Integer> nums = Arrays.stream(bufferedReader.readLine().split(" "))
                    .map(Integer::parseInt)
                    .collect(Collectors.toList());

            minimumBribe(nums);
        }

        bufferedReader.close();
    }
}
