// 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.
package BaekJoon;

import java.util.Scanner;
public class 브론즈_3052_나머지 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[42];

        for (int i = 0; i < 10; i++) {
            int num = sc.nextInt();
            int mod = num % 42;
            arr[mod] += 1;
        }

        int cnt = 0;
        for (int i = 0; i < 42; i++) {
            if (arr[i] > 0) {
                cnt += 1;
            }
        }
        System.out.println(cnt);
    }
}
