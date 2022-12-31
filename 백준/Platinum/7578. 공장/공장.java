import java.io.*;
import java.util.*;

public class Main {

    static int N, S;
    static int MAX = 1000000;
    static int[] A, B;
    static long ans = 0;
    static long[] tree;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        S = 1;
        while(S < MAX){
            S *= 2;
        }
        tree = new long[S*2];

        A = new int[MAX + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            A[Integer.parseInt(st.nextToken())] = i;
        }

        B = new int[N + 1];
        st = new StringTokenizer(br.readLine());

        for (int i = 1; i <= N; i++) {
            int b = Integer.parseInt(st.nextToken());
            B[i] = A[b];
        }

        for (int i = 1; i <= N; i++) {
            int val = B[i];

            ans += query(1, N,1, val+1, N);
            update(1, N, 1, val);
        }

        System.out.println(ans);
    }

    public static long query(int start, int end, int node, int queryLeft, int queryRight){
        if((end < queryLeft) || (start > queryRight)) return 0;

        if((queryLeft <= start) && (end <= queryRight)) return tree[node];

        int mid = (start + end) /2;
        return query(start, mid, node * 2, queryLeft, queryRight) + query(mid + 1, end, node * 2 + 1, queryLeft, queryRight);
    }

    public static void update(int left, int right, int node, int target){
        if(target < left || target > right) return;

        tree[node]++;
        if (left != right){
            int mid = (left + right) / 2;
            update(mid+1, right, node * 2 + 1, target);
            update(left, mid, node * 2, target);
        }

    }
}
