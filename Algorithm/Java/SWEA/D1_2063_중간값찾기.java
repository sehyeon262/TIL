import java.util.Scanner;
import java.io.FileInputStream;
import java.util.Arrays;

public class D1_2063_중간값찾기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int[] arr = new int[N];
        
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();                    
        }

        // 정렬
        Arrays.sort(arr);

        System.out.println(arr[N / 2]);
    }
}
