import java.util.Scanner;
public class 브론즈_27866_문자와문자열 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String str = sc.next();
        int n = sc.nextInt();
        char c = str.charAt(n-1);
        System.out.println(c);
    }
}
