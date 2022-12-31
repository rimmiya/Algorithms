import java.util.*;
import java.io.*;

public class Main {

    static int N;
    static int[] A;
    static int[] dp;
    static int[] list;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        A = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        int LIS = 0;
        dp = new int[N];
        list = new int[N+1];
        list[0] = -1000000001;
        for (int i = 0; i < N; i++) {
            if(list[LIS] < A[i]) {
                dp[i] = ++LIS;
                list[LIS] = A[i];
            } else {
                int idx = BinarySearch(A[i], 0, LIS);
                list[idx] = A[i];
                dp[i] = idx;
            }
        }
        StringBuilder sb = new StringBuilder();
        sb.append(LIS+"\n");

        Stack<Integer> s = new Stack<>();
        for (int i = N-1; i >= 0; i--) {
            if(dp[i] == LIS){
                s.push(A[i]);
                LIS--;
            }
        }

        while (!s.isEmpty()){
            sb.append(s.pop()+" ");
        }
        System.out.println(sb.toString());
    }

    public static int BinarySearch(int num, int start, int end){
        while (start < end){
            int mid = (start + end) / 2;
            if(num <= list[mid]){
                end = mid;
            } else {
                start = mid + 1;
            }
        }

        return end;
    }
}
