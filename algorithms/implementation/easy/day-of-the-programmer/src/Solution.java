import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class Solution {
    static final String LEAP_YEAR_FORMAT = "12.09.%d";
    static final String REGULAR_YEAR_FORMAT = "13.09.%d";

    static String gregorian(int year) {
        if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)) {
            return String.format(LEAP_YEAR_FORMAT, year);
        }

        return String.format(REGULAR_YEAR_FORMAT, year);
    }

    static String julian(int year) {
        if (year % 4 == 0) {
            return String.format(LEAP_YEAR_FORMAT, year);
        }

        return String.format(REGULAR_YEAR_FORMAT, year);
    }

    // Complete the dayOfProgrammer function below.
    static String dayOfProgrammer(int year) {
        if (year == 1918) {
            return "26.09.1918";
        } else if (year > 1918) {
            return gregorian(year);
        }

        return julian(year);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int year = Integer.parseInt(bufferedReader.readLine().trim());

        String result = dayOfProgrammer(year);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
