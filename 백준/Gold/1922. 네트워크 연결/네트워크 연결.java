import java.util.*;
import java.io.*;

public class Main {

    static int N, M;
    static int a, b, cost;
    static int[] parent;
    static int result;
    static PriorityQueue<Edge> pq;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        // self loop로 초기화
        parent = new int[N+1];
        for (int i = 1; i <= N; i++) {
            parent[i] = i;
        }

        pq = new PriorityQueue<Edge>();
        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            cost = Integer.parseInt(st.nextToken());

            pq.add(new Edge(a, b, cost));
        }

        while (!pq.isEmpty()){
            Edge tmp = pq.poll();

            if(find(tmp.start) != find(tmp.end)){
                union(tmp.start, tmp.end);
                result += tmp.value;
            }
        }
        System.out.println(result);
    }

    public static int find(int x){
        if(x == parent[x]){
            return x;
        }
        return parent[x] = find(parent[x]);
    }

    public static void union(int x, int y){
        x = find(x);
        y = find(y);

        if(x != y){
            parent[x] = y;
        }
    }
}

class Edge implements Comparable<Edge>{
    int start;
    int end;
    int value;

    public Edge(int start, int end, int value){
        this.start = start;
        this.end = end;
        this.value = value;
    }

    @Override
    public int compareTo(Edge o) {
        return o.value > this.value ? -1 : 1;
    }
}
