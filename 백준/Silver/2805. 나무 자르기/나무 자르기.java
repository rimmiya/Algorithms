import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");

        int N = Integer.parseInt(str[0]); // 나무의 수
        int M = Integer.parseInt(str[1]); // 집에 가져갈 나무의 길이

        str = br.readLine().split(" ");
        int[] tree = new int[N];
        int min = 0;
        int max = 0;

        for(int i = 0; i < N; i++){
            tree[i] = Integer.parseInt(str[i]);

            if(max < tree[i]){
                max = tree[i];
            }
        }

        while(min < max){
            int mid = (min + max) / 2;
            long sum = 0;
            for (int i = 0; i < N; i++) {
                if((tree[i] - mid) > 0){
                    sum += tree[i] - mid;
                }
            }
            if(sum < M){
                max = mid;
            } else {
                min = mid + 1;
            }
        }
        System.out.println(min - 1);
    }
}
