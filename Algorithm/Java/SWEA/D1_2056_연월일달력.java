import java.util.Scanner;
import java.io.FileInputStream;

public class D1_2056_연월일달력 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int t = 1; t < T+1; t++) {
            String date = sc.next();

            int year = Integer.parseInt(date.substring(0,4));
            int month = Integer.parseInt(date.substring(4,6));
            int day = Integer.parseInt(date.substring(6,8));

            boolean valid = true;

            if (month < 1 || month > 12) {
                valid = false;
            }
            else if (month == 2) {    
                if (day < 1 || day > 28)
                    valid = false;
            }
            else if (month == 4 || month == 6 || month == 9 || month == 11) {
                if (day < 1 || day > 30)
                    valid = false;
            }
            else {
                if (day < 1 || day > 31)
                    valid = false;
            }

            if (valid) {
                System.out.printf("#%d %04d/%02d/%02d\n", t, year, month, day);
            } 
            else 
                System.out.println("#" + t + " " + -1);
        }
    }
}
