import java.io.*;
import java.util.*;

public class Main {

    static int N, M;
    static long[] weight;
    static int[] parent;
    static long result;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true){
            st  = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            if(N == 0 && M == 0){
                break;
            }

            weight = new long[N+1];
            parent = new int[N+1];
            for (int i = 1; i <= N; i++) {
                parent[i] = i;
            }
            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                char cmd = st.nextToken().charAt(0);
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());

                if(cmd == '!'){
                    int diff = Integer.parseInt(st.nextToken());
                    union(a, b, diff);
                } else if (cmd == '?'){
                    if(find(a) == find(b)){
                        result = weight[b] - weight[a];
                        System.out.println(result);
                    } else {
                        System.out.println("UNKNOWN");
                    }

                }
            }
        }
    }

    public static int find(int a){
        if(a == parent[a]){
            return a;
        } else{
            int idx = find(parent[a]);
            weight[a] += weight[parent[a]];
            return parent[a] = idx;
        }
    }

    public static void union(int a, int b, int diff){
        int parentA = find(a);
        int parentB = find(b);

        if(parentA != parentB){
            weight[parentB] = weight[a] - weight[b] + diff;
            parent[parentB] = parentA;
        }
    }
}
