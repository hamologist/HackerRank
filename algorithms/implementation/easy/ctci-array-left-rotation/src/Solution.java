import java.io.*;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;

public class Solution {
    public static LinkedList<String> rotLeft(LinkedList<String> target, int rotations) {
        for (int i = 0; i < rotations; i++) {
            target.addLast(target.pop());
        }

        return target;
    }

    public static void main(String []args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        List<Integer> pairs = Arrays.stream(bufferedReader.readLine().split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toList());

        int d = pairs.get(1);

        LinkedList<String> target = Arrays.stream(bufferedReader.readLine().split(" "))
                .collect(Collectors.toCollection(LinkedList::new));

        bufferedWriter.write(String.join(" ", rotLeft(target, d)));

        bufferedReader.close();
        bufferedWriter.close();
    }
}
