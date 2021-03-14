import java.io.*;

public class Solution {
    final static char UP = 'U';
    final static char DOWN = 'D';

    public static int countingValleys(char[] path) {
        int valleys = 0;
        int level = 0;

        for (char step: path) {
            if (step == UP) {
                level++;

                if (level == 0) {
                    valleys++;
                }
            } else if (step == DOWN) {
                level--;
            }
        }

        return valleys;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        bufferedReader.readLine();
        char[] path = bufferedReader.readLine().toCharArray();

        int valleys = countingValleys(path);
        bufferedWriter.write(String.valueOf(valleys));

        bufferedReader.close();
        bufferedWriter.close();
    }
}
