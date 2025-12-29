import java.util.Scanner;
import java.io.FileInputStream;

public class D1_1933_간단한N의약수 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 1; i < n + 1; i++) {
            if (n % i == 0)
                System.out.print(i + " ");
        }
    }
}
