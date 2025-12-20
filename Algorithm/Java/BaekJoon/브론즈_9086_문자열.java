import java.util.Scanner;
public class 브론즈_9086_문자열 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int i = 0; i < T; i++) {
            String str = sc.next();
            char start = str.charAt(0);
            char end = str.charAt(str.length() - 1);
            // char + char => 아스키 코드 덧셈 됨
            // 따라서 빈문자열 붙인 후 연결해야함!
            System.out.println("" + start + end);
        }
    }
}
