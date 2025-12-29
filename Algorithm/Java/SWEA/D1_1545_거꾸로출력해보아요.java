import java.util.Scanner;
import java.io.FileInputStream;

public class D1_1545_거꾸로출력해보아요 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = n; i >= 0; i--)
            System.out.print(i + " ");
    }
}
