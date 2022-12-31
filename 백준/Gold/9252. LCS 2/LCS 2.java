import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static char[] A, B;
    static int[][] dp;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        A = br.readLine().toCharArray();
        B = br.readLine().toCharArray();

        dp = new int[A.length+1][B.length+1];
        for (int i = 0; i <= A.length; i++) {
            for (int j = 0; j <= B.length; j++) {
                if(i == 0 || j == 0){
                    dp[i][j] = 0;
                } else if(A[i-1] == B[j-1]){
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else{
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }

        int i = A.length;
        int j = B.length;
        char[] result = new char[dp[i][j]];
        int k = 0;
        while (dp[i][j] != 0){
            if(dp[i][j] == dp[i-1][j]){
                i -= 1;
            } else if(dp[i][j] == dp[i][j-1]){
                j -= 1;
            } else{
                result[k++] = A[i-1];
                i -= 1;
                j -= 1;
            }
        }

        System.out.println(k);
        StringBuilder sb = new StringBuilder();
        for (int l = k-1; l >=0 ; l--) {
            sb.append(result[l]);
        }
        System.out.println(sb);
    }
}
