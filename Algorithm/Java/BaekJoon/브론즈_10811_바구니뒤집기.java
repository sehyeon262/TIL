import java.util.Scanner;
public class 브론즈_10811_바구니뒤집기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = i + 1;
        }
        
        // 뒤집기
        for (int a = 0; a < m; a++) {
            int i = sc.nextInt() - 1;
            int j = sc.nextInt() - 1;

            for (; i < j; i++, j--) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        
        // for-each문 : 배열이나 리스트에 있는 값을 하나씩 꺼내는 반복문
        for (int x : arr) {
            System.out.print(x + " ");
        }
    }
}
