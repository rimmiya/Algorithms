import java.util.*;
import java.io.*;

public class Main {

    static int N;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        MaxHeap mh = new MaxHeap();

        for (int i = 0; i < N; i++) {
            int x = Integer.parseInt(br.readLine());
            if(x == 0){
                System.out.println(mh.delete());
            } else {
                mh.insert(x);
            }
        }
    }
}

class MaxHeap{
    List<Integer> list;

    public MaxHeap(){
        list = new ArrayList<>();
        list.add(0); // 0번 사용 X -> index 1번부터 사용
    }

    public void insert(int val){
        // 1. leaf 마지막에 삽입
        list.add(val); // list는 add하면 제일 마지막에 삽입됨

        // 2. 부모와 비교 후 조건에 마지 않으면 Swap
        int current = list.size() - 1;
        int parent = current / 2;

        // 3. 조건이 만족되거나 root 까지 반복
        while(true){
            if(parent == 0 || list.get(parent) >= list.get(current)){
                break;
            }

            // Swap
            int tmp = list.get(parent);
            list.set(parent, list.get(current));
            list.set(current, tmp);

            current = parent;
            parent = current / 2;
        }
    }

    public int delete(){
        if(list.size() == 1){ // 비어있다
            return 0;
        }

        int top = list.get(1);

        // 1. Root 에 leaf 마지막 데이터 가져옴
        list.set(1, list.get(list.size() -1));
        list.remove(list.size() - 1);

        // 2. 자식과 비교 후 조건이 맞지 않으면 Swap
        // 3. 조건이 만족되거나 leaf 까지 반복
        int currentPos = 1;
        while (true){
            int leftPos = currentPos * 2;
            int rightPos = currentPos * 2 + 1;

            // 자식 존재 유무 확인
            if(leftPos >= list.size()){ // 자식이 없는 경우
                break;
            }

            // 왼쪽 자식 먼저 확인
            int minValue = list.get(leftPos);
            int minPos = leftPos;

            // 오른쪽 자식 확인
            // left node 먼저 안보면 index 오류 발생 가능
            if(rightPos < list.size() && list.get(rightPos) > minValue){
                minValue = list.get(rightPos);
                minPos = rightPos;
            }

            // Swap
            if(list.get(currentPos) < minValue){
                int tmp = list.get(currentPos);
                list.set(currentPos, list.get(minPos));
                list.set(minPos, tmp);
                currentPos = minPos;
            } else {
                break;
            }
        }

        return top;
    }
}
