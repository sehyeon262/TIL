import java.util.Scanner;

public class 브론즈_1152_단어의개수 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = 0;
        
        String str = sc.nextLine().trim();

        if (str.isEmpty()) {
            System.out.println(0);
        }
        else {
            String[] words = str.split(" ");
            System.out.println(words.length);
        }
    }
}
