import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;

class Pair {
    int num;
    String value;

    public Pair(int num, String value) {
        this.num = num;
        this.value = value;
    }

    public int getNum() {
        return num;
    }

    public String getValue() {
        return value;
    }
}

public class Solution {

    // Complete the countSort function below.
    static void countSort(List<Pair> arr) {
        arr.sort(Comparator.comparing(Pair::getNum));

        String result = arr.stream()
                .map(Pair::getValue)
                .collect(Collectors.joining(" "));
        System.out.println(result);
    }

    public static void main(String[] args) throws IOException {
        List<Pair> arr = new ArrayList<>();
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine());
        for (int i = 0; i < n; i++) {
            String[] pair = bufferedReader.readLine().split(" ");

            if (i < n / 2) {
                pair[1] = "-";
            }

            arr.add(new Pair(Integer.parseInt(pair[0]), pair[1]));
        }
        countSort(arr);

        bufferedReader.close();
    }
}
