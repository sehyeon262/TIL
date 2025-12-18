package BaekJoon;

import java.util.Scanner;
public class 브론즈_10813_공바꾸기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 1; i < n+1; i++) {
            arr[i-1] = i;
        }

        for (int a = 0; a < m; a++) {
            int i = sc.nextInt();
            int j = sc.nextInt();
            int temp = arr[i-1];
            arr[i-1] = arr[j-1];
            arr[j-1] = temp;
        }

        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
