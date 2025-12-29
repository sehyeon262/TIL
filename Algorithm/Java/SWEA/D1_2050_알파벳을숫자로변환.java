import java.util.Scanner;
import java.io.FileInputStream;

public class D1_2050_알파벳을숫자로변환 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();

        for (int i = 0; i < str.length(); i++) {
            System.out.print(str.charAt(i) - 64 + " ");
        }
    }
}
