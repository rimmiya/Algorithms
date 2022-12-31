import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        System.out.println(arithmetic_sequence(N));
    }

    public static int arithmetic_sequence(int N){
        int cnt = 0;

        if(N < 100){
            return N;
        } else {
            if(N == 1000){
                N = 999;
            }
            for (int i = 100; i <= N; i++) {
                int hun = i / 100;
                int ten = (i / 10) % 10;
                int one = i % 10;
                if((hun - ten) == (ten - one)){
                    cnt++;
                }
            }
            cnt += 99;
        }
        return cnt;
    }
}
