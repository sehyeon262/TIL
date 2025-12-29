import java.util.Scanner;
import java.io.FileInputStream;

public class D1_2060_최대수구하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int t = 1; t < T+1; t++) {
            int max = 0;

            for (int i = 0; i < 10; i++) {
                int num = sc.nextInt();
                
                if (max < num)
                    max = num;
            }
            System.out.println("#" + t + " " + max);
        }
    }
}
