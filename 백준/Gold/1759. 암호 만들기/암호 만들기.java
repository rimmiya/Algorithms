import java.util.*;

import javax.swing.text.AbstractDocument.BranchElement;

import java.io.*;
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;

public class Main {
	
	static int L, C;
	static char arr[];
	static char key[];
	static StringBuilder sb;
	static BufferedWriter bw;
	
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
// 		bw = new BufferedWriter(new OutputStreamWriter(System.out));
		sb = new StringBuilder();
		
		String[] s = br.readLine().split(" ");
		L = Integer.valueOf(s[0]);
		C = Integer.valueOf(s[1]);
		
		key = new char[L];
		arr = new char[C];
		s = br.readLine().split(" ");
		for(int i = 0; i < C; i++) {
			arr[i] = s[i].charAt(0);
		}
		Arrays.sort(arr);	
		dfs(0, 0, 0, 0);
        System.out.print(sb);
	}
	
	private static void dfs(int idx, int cnt, int v, int c) {
		// 목적지인가 
		if(cnt == L) {
			if(v >= 1 && c >= 2) {
				for(int i = 0; i < L; i++){
				    sb.append(key[i]);
				}
				sb.append("\n");
			}
			return;
		}
		for(int i = idx; i < C; i++) {
			key[cnt] = arr[i];
			if(arr[i] == 'a' || arr[i] == 'e' || arr[i] == 'i' || arr[i] == 'o' || arr[i] == 'u') {
				dfs(i+1, cnt+1, v+1, c);
			}
			else {
				dfs(i+1, cnt+1, v, c+1);
			}
				
		}
	}

}
