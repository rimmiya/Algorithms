import java.util.*;
import java.io.*;

public class Main {

    static int N;
    static int[] list;
    static int[] LR;
    static int[] RL;
    static int num;
    static int result;
    static int temp;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        list = new int[N];
        LR = new int[N];
        RL = new int[N];
        for (int n = 0; n < N; n++) {
            list[n] = Integer.parseInt(st.nextToken());
            if(n == 0){
                LR[n] = list[n];
            }
            else{
                LR[n] = gcd(LR[n-1], list[n]);
            }
        }
        for (int n = N-1; n > 0; n--) {
            if(n == N-1){
                RL[n] = list[n];
            } else{
                RL[n] = gcd(RL[n+1], list[n]);
            }
        }
        RL[0] = gcd(RL[1], list[0]);

        result = 0;
        for (int i = 0; i < N; i++) {
            if(i == 0){
                temp = RL[i+1];
            } else if(i == N-1){
                temp = LR[i-1];
            } else{
                temp = gcd(LR[i-1], RL[i+1]);
            }

            if(temp > result){
                num = i;
                result = temp;
            }
        }

        if(list[num] % result == 0){
            System.out.println("-1");
        } else{
            System.out.println(result + " " + list[num]);
        }
    }

    public static int gcd(int a, int b){
        int r = a % b;
        if(r == 0){
            return b;
        } else{
            return gcd(b, r);
        }
    }
}
