// S2 : 1713 후보 추천하기
import java.util.*;
import java.io.*;

public class Main {
    static int N, K;
    static Person[] people;

    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();

        people = new Person[101];

        List<Person> list = new ArrayList<>();
        for (int k = 0; k < K; k++) {
            int num = sc.nextInt();
            if(people[num] == null){ // 처음 추천 받은 학생 -> 객체 생성
                people[num] = new Person(num, 0,0,false);
            }
            // 이미 게시된 경우
            if(people[num].isPosted){
                people[num].count++;
            }
            // 게시된 적 없음
            else{
                // 게시판이 꽉 찬 경우 -> 추천수 적은 친구 -> 같으면 오래된 친구
                if(list.size()==N){
                    Collections.sort(list);
                    Person p = list.remove(0);
                    p.isPosted = false;
                }
                // 게시판에 추가
                people[num].count = 1;
                people[num].timestamp = k;
                people[num].isPosted = true;
                list.add(people[num]);
            }
        }

        Collections.sort(list, Comparator.comparingInt(o -> o.num));

        for(Person p : list){
            System.out.print(p.num + " ");
        }
    }
}

class Person implements Comparable<Person>{
    int num;
    int count;
    int timestamp;
    boolean isPosted;

    public Person(int num, int count, int timestamp, boolean isPosted){
        this.num = num;
        this.count = count;
        this.timestamp = timestamp;
        this.isPosted = isPosted;
    }

    @Override
    public int compareTo(Person o) {
        int comp1 = Integer.compare(count, o.count);
        if(comp1 == 0){
            return Integer.compare(timestamp, o.timestamp);
        } else {
            return comp1;
        }
    }
}
