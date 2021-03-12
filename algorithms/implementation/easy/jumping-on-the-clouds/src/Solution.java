import java.io.*;

public class Solution {
    final static char SAFE = '0';

    public static int jumpingOnClouds(char[] cloudState) {
        int jumps = 0;
        int position = 0;

        while (position != cloudState.length-1) {
            if (position + 2 < cloudState.length && cloudState[position + 2] == SAFE) {
                position += 2;
            } else {
                position += 1;
            }

            jumps++;
        }

        return jumps;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        bufferedReader.readLine();
        char[] cloudState = bufferedReader.readLine().replace(" ", "").toCharArray();

        bufferedWriter.write(String.valueOf(jumpingOnClouds(cloudState)));

        bufferedReader.close();
        bufferedWriter.close();
    }
}
