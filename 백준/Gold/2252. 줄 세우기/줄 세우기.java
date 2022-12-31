import java.io.*;
import java.util.*;

public class Main {

    static int N, M;


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        LinkedList<Integer>[] list = new LinkedList[N+1]; // 노드의 연결상태 저장
        int[] link = new int[N+1]; // 조건의 개수를 저장
        for (int i = 1; i <= N; i++) {
            list[i] = new LinkedList<>();
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            list[a].add(b);
            link[b]++;
        }

        Queue<Integer> queue = new LinkedList<Integer>();
        for (int i = 1; i <= N; i++) {
            if(link[i] == 0){
                queue.add(i);
            }
        }

        while (!queue.isEmpty()){
            System.out.print(queue.peek()+" ");
            int q = queue.poll();

            for (int i = 0; i < list[q].size(); i++) {
                int next = list[q].get(i);
                link[next]--;
                if(link[next] == 0){
                    queue.add(next);
                }
            }
        }
    }
}
