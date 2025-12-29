import java.util.Scanner;
import java.io.FileInputStream;

public class D1_2058_자릿수더하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();

        int N = str.length();
        int sum = 0;

        for (int i = 0; i < N; i++) {
            int a = str.charAt(i) - '0';
            sum += a;
        }
        System.out.println(sum);
    }
}
