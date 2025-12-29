import java.util.Scanner;
import java.io.FileInputStream;

public class D1_2025_N줄덧셈 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0;

        for (int i = 1; i < n + 1; i++) {
            sum += i;
        }
        System.out.println(sum);
    }
}
