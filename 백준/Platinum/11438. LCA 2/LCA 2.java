import java.util.ArrayList;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

    static int maxHeight = 17;
    static int N, M;
    static int[] Depth;
    static int[][] Parent;
    static ArrayList<Integer>[] list;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        list = new ArrayList[N+1];
        for (int i = 0; i < N+1; i++) {
            list[i] = new ArrayList<>();
        }

        for (int i = 0; i < N-1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            list[a].add(b);
            list[b].add(a);
        }

        Depth = new int[N+1];
        Parent = new int[maxHeight][N+1];

        init(1, 1, 0);
        fillParents();

        StringBuilder sb = new StringBuilder();
        M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            sb.append(LCA(a, b) + "\n");
        }

        System.out.println(sb.toString());
    }
    static void init(int cur, int h, int pa){
        Depth[cur] = h;

        for(int next : list[cur]){
            if(next != pa){
                init(next, h+1, cur);
                Parent[0][next] = cur;
            }
        }
    }

    static void fillParents(){
        for (int i = 1; i < maxHeight; i++) {
            for (int j = 1; j < N+1; j++) {
                Parent[i][j] = Parent[i-1][Parent[i-1][j]];
            }
        }
    }

    static int LCA(int a, int b){
        int ah = Depth[a];
        int bh = Depth[b];

        // ah > bh로 세팅
        if(ah < bh){
            int tmp = a;
            a = b;
            b = tmp;
        }

        // 높이 맞춰주기
        for (int i = maxHeight-1; i >= 0 ; i--) {
            int diff = Depth[a] - Depth[b];
            if(Math.pow(2, i) <= diff){
                a = Parent[i][a];
            }
        }

        if(a == b) return a;

        // LCA 찾기
        for (int i = maxHeight-1; i >= 0; i--) {
            if(Parent[i][a] != Parent[i][b]){
                a = Parent[i][a];
                b = Parent[i][b];
            }
        }

        return Parent[0][a];
    }
}
