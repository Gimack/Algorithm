import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.*;
import java.util.*;

public class Main {
    static String[][] arr = new String[101][101];
    static boolean[][] check = new boolean[101][101];
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {-1, 1, 0, 0};
    static int T, count, count2;
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        count = 0;
        count2 = 0;
        for(int i = 0; i < T; i++) {
            String[] input = br.readLine().split("");
            for(int j = 0; j < T; j++) {
                arr[i][j] = input[j];
            }
        }
        // 정상
        for(int i = 0; i < T; i++) {
            for(int j = 0; j < T; j++) {
                if(!check[i][j]) {
                    count++;
                    DFS(i, j);
                }
            }
        }
        // 적록색약
        for(int i = 0; i < T; i++) {
            for(int j = 0; j < T; j++) {
                if(arr[i][j].equals("R")) {
                    arr[i][j] = "G";
                }
                check[i][j] = false; // 초기화
            }
        }
        for(int i = 0; i < T; i++) {
            for(int j = 0; j < T; j++) {
                if(!check[i][j]) {
                    count2++;
                    DFS(i, j);
                }
            }
        }
        System.out.print(count + " " + count2);

    }
    public static void DFS(int x, int y) {
        check[x][y] = true;
        String c = arr[x][y];
        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(0 <= nx && nx < T && 0 <= ny && ny < T) {
                if(arr[nx][ny].equals(c) && !check[nx][ny]) {
                    DFS(nx, ny);
                }
            }
        }
    }
}
