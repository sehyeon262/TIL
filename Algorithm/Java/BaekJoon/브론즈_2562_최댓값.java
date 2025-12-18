package BaekJoon;

import java.util.Scanner;
public class 브론즈_2562_최댓값 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cnt = 0;
        int max = 0;

        for (int i = 0; i < 9; i++) {
            int num = sc.nextInt();
            if (num > max) {
                max = num;
                cnt = i+1;
            }
        }
        System.out.println(max);
        System.out.println(cnt);

    }
}
