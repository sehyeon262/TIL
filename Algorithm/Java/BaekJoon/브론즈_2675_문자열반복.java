import java.util.Scanner;

public class 브론즈_2675_문자열반복 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt(); // 테스트케이스

        for (int t = 0; t < T; t++) {
            int r = sc.nextInt();
            String str = sc.next();

            for (int i = 0; i < str.length(); i++) {
                for (int j = 0; j < r; j++) {
                    System.out.print(str.charAt(i));
                }
            }
            System.out.println();
        }
    }
}
