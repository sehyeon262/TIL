import java.util.Scanner;

public class D1_2071_평균값 구하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int t = 1; t < T+1; t++) {
            int sum = 0;

            for (int i = 0; i < 10; i++) {
                int num = sc.nextInt();
                sum += num;
            }
            double avg = sum / 10.0;
    
            System.out.printf("%d" "%.0f", t, avg);
        }
    }
}
