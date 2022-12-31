import java.io.*;

public class Main {

    static int N, M;
    static String[] string;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");

        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);

        string = br.readLine().split(" ");

        int cnt = 0;
        for (int n = 0; n < N; n++) {
            int sum = 0;
            int low = n;
            for(int i = low; i < string.length; i++){
                sum += Integer.parseInt(string[i]);
                if(sum == M) {
                    low ++;
                    cnt ++;
                } else if(sum < M){
                    continue;
                } else {
                    low ++;
                }
            }
        }
        System.out.println(cnt);
    }
}
