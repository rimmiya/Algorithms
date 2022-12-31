import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> maxPQ = new PriorityQueue<>(Comparator.reverseOrder());
        PriorityQueue<Integer> minPQ = new PriorityQueue<>();

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            int n = Integer.parseInt(br.readLine());
            if(maxPQ.size() == minPQ.size()){
                maxPQ.add(n);
            } else{
                minPQ.add(n);
            }

            if(!minPQ.isEmpty() && !maxPQ.isEmpty()){
                if(minPQ.peek() < maxPQ.peek()){
                    int tmp = minPQ.poll();
                    minPQ.offer(maxPQ.poll());
                    maxPQ.offer(tmp);
                }
            }
            
            sb.append(maxPQ.peek()+"\n");
        }

        System.out.println(sb.toString());
    }
}
