import java.util.Scanner;
import java.io.FileInputStream;

public class D1_2029_몫과나머지출력하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        for (int t = 1; t < T + 1; t++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            int div = a / b;
            int mod = a % b;
            System.out.println("#" + t + " " + div + " " + mod);
        }
    }
}
