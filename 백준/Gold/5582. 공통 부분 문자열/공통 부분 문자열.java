import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static char[] A, B;
    static int[][] dp;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        A = br.readLine().toCharArray();
        B = br.readLine().toCharArray();

        dp = new int[A.length+1][B.length+1];
        int max = 0;
        for (int i = 0; i <= A.length; i++) {
            for (int j = 0; j <= B.length; j++) {
                if(i == 0 || j == 0){
                    dp[i][j] = 0;
                } else if(A[i-1] == B[j-1]){
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else{
                    dp[i][j] = 0;
                }

                if(max < dp[i][j]) {
                    max = dp[i][j];
                }
            }
        }

        System.out.println(max);
    }
}
