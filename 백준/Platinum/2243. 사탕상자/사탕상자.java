import java.util.*;
import java.io.*;

public class Main {

    static int N, M;
    static int A, B, C;
    static int MAX = 1000000;
    static int[] tree;
    static int S;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        S = 1;
        while(S < MAX){
            S *= 2;
        }
        tree = new int[S * 2];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            A = Integer.parseInt(st.nextToken());
            if(A == 2){
                B = Integer.parseInt(st.nextToken());
                C = Integer.parseInt(st.nextToken());
                update(1,S,1, B, C);
            } else if (A == 1){
                B = Integer.parseInt(st.nextToken());
                int index = query(1, S,1, B);
                update(1, S, 1, index, -1);
                System.out.println(index);
            }
        }

    }

    static int query(int left, int right, int node, int count){
        if(left == right){
            return left;
        }
        int mid = (left + right) / 2;
        if(tree[node * 2] >= count){
            return query(left, mid, node * 2, count);
        }
        else{
            return query(mid + 1, right, node * 2 + 1, count - tree[node*2]);
        }
    }

    static void update(int left, int right, int node, int target, long diff){
        if(left <= target && target <= right){
            tree[node] += diff;
            if(left != right){
                int mid = (left + right) / 2;
                update(left, mid, node * 2, target, diff);
                update(mid + 1, right, node * 2 + 1, target, diff);
            }
        }
    }
}
