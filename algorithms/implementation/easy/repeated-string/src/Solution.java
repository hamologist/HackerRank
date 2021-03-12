import java.io.*;

public class Solution {
    public static long repeatedString(String repeater, long length) {
        long aCountInRepeater = repeater.chars().filter(ch -> ch == 'a').count();
        long aCount = aCountInRepeater * (length / repeater.length());

        for (int i = 0; i < length % repeater.length(); i++) {
            if (repeater.charAt(i) == 'a') {
                aCount++;
            }
        }

        return aCount;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String repeater = bufferedReader.readLine();
        long length = Long.parseLong(bufferedReader.readLine());

        bufferedWriter.write(String.valueOf(repeatedString(repeater, length)));

        bufferedReader.close();
        bufferedWriter.close();
    }
}
