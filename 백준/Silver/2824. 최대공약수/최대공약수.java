import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {

    static int N, M;
    static BigInteger A, B;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        A = BigInteger.ONE;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int n = 0; n < N; n++) {
            A = A.multiply(new BigInteger(st.nextToken()));
        }

        M = Integer.parseInt(br.readLine());

        B = BigInteger.ONE;
        st = new StringTokenizer(br.readLine());
        for (int m = 0; m < M; m++) {
            B = B.multiply(new BigInteger(st.nextToken()));
        }

        String gcd = A.gcd(B).toString();

        System.out.println(gcd.length() > 9 ? gcd.substring(gcd.length()-9, gcd.length()) : gcd);
    }
}
