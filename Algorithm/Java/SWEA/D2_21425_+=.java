import java.util.Scanner;
import java.io.FileInputStream;

public class D2_21425_+= {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int t = 1; t < T+1; t++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int N = sc.nextInt();

            int cnt = 0;

            while (a <= N && b <= N) {
                if (a < b) {
                    a += b;
                } else {
                    b += a;
                }
                cnt++;
            }
            System.out.println(cnt);
        }
    }
}
                     