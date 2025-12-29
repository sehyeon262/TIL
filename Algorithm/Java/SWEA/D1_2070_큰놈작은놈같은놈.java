import java.util.Scanner;
import java.io.FileInputStream;

public class D1_2070_큰놈작은놈같은놈 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int t = 1; t < T+1; t++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            if (a < b)
                System.out.println("#" + t + " <");
            else if (a == b)
                System.out.println("#" + t + " =");
            else
                System.out.println("#" + t + " >");
        }
    }
}
