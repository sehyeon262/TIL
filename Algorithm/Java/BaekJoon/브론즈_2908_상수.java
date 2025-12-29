import java.util.Scanner;

public class 브론즈_2908_상수 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str1 = sc.next();
        String str2 = sc.next();

        // 문자열 뒤집기
        // StringBuilder: 가변 문자열 -> 내용 변경 가능!
        // 뒤집고 문자열로 만들기
        String rev1 = new StringBuilder(str1).reverse().toString();
        String rev2 = new StringBuilder(str2).reverse().toString();

        // Integer.parseInt() : 문자열 -> 숫자 변환
        int num1 = Integer.parseInt(rev1);
        int num2 = Integer.parseInt(rev2);

        System.out.println(Math.max(num1, num2));
    }
}