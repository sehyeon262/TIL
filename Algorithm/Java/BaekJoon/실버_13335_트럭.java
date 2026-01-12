// 각 트럭들은 하나의 단위시간(unit time)에 하나의 단위길이만큼만 이동할 수 있다고 가정한다. 
// 동시에 다리 위에 올라가 있는 트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야 한다.

import java.util.Scanner;

public class 실버_13335_트럭 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();  // 트럭의 수
        int w = sc.nextInt();  // 다리 길이
        int L = sc.nextInt();  // 다리의 최대하중
        int[] truck = new int[n];

        for (int i = 0; i < n; i++) {
            truck[i] = sc.nextInt();
        }

        int total = 0;

        for (int i = 0; i < n; i ++) {
            if (total <= L) {

            }

        }

    }
}
