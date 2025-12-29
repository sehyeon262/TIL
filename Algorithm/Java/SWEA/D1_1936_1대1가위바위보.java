import java.util.Scanner;
import java.io.FileInputStream;

public class D1_1936_1대1가위바위보 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        // 가위 1, 바위 2, 보 3
        if ((a == 2 && b == 1) || (a == 1 && b == 3) || (a == 3 && b == 2)) {
            System.out.println("A");
        }
        else 
            System.out.println("B");

    }
}
