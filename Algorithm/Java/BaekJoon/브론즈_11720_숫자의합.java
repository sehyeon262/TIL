import java.util.Scanner;

public class 브론즈_11720_숫자의합 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String num = sc.next();
        
        int sum = 0;
        for (int i = 0; i < n; i++) {
            // charAt()은 유니코드로 저장되므로
            // '5'(53) - '0'(43) = 5 (숫자로 변환됨!!)
            sum += num.charAt(i) - '0';  
        }
        System.out.println(sum);
    }
}