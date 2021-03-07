import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the surfaceArea function below.
    static int surfaceArea(int[][] A) {
        int totalSurfaceArea = 0;
        int surfaceArea;
        int l;
        int neighbor;

        for (int y = 0; y < A.length; y++) {
            for (int x = 0; x < A[y].length; x++) {
                l = A[y][x];
                surfaceArea = 2 + (4 * l);

                if (y - 1 >= 0) {
                    neighbor = A[y-1][x];
                    surfaceArea = surfaceArea - Math.min(l, neighbor);
                }

                if (y + 1 < A.length) {
                    neighbor = A[y+1][x];
                    surfaceArea = surfaceArea - Math.min(l, neighbor);
                }

                if (x - 1 >= 0) {
                    neighbor = A[y][x-1];
                    surfaceArea = surfaceArea - Math.min(l, neighbor);
                }

                if (x + 1 < A[y].length) {
                    neighbor = A[y][x+1];
                    surfaceArea = surfaceArea - Math.min(l, neighbor);
                }

                totalSurfaceArea += surfaceArea;
            }
        }

        return totalSurfaceArea;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] HW = scanner.nextLine().split(" ");

        int H = Integer.parseInt(HW[0]);

        int W = Integer.parseInt(HW[1]);

        int[][] A = new int[H][W];

        for (int i = 0; i < H; i++) {
            String[] ARowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < W; j++) {
                int AItem = Integer.parseInt(ARowItems[j]);
                A[i][j] = AItem;
            }
        }

        int result = surfaceArea(A);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
