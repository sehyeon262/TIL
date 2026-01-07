// 2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.
// 비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?

import java.util.Scanner;

public class 골드_14719_빗물 {
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int H = sc.nextInt(); // 세로
        int W = sc.nextInt(); // 가로
        
        int[] arr = new int[W];  // 각 칸의 블록 높이를 저장할 배열만듦

        // W개의 높이 입력 받음
        for (int i = 0; i < W; i++) {
            arr[i] = sc.nextInt();
        }

        int sum = 0;  // 빗물이 고이는 총량

        // 현재 칸에 물이 고이려면 ???
        // 1. 왼쪽에서 가장 높은 벽 구함 (L)
        // 2. 오른쪽에서 가장 높은 벽 구함 (R)
        // 3. L과 R 중 낮은 높이만큼 물이 참. (min)
        // 4. (min - 현재 내 높이) 만큼 물이 참
        
        for (int i = 1; i < W-1; i++) {
            int Lmax = 0;
            int Rmax = 0;

            // 오른쪽 최대높이
            for (int j = i + 1; j < W; j++) {
                Rmax = Math.max(Rmax, arr[j]);
            }

            // 왼쪽 최대높이
            for (int j = 0; j < i; j++) {
                Lmax = Math.max(Lmax, arr[j]);
            }

            int min = Math.min(Lmax, Rmax);
            int water = min - arr[i];

            if (water > 0) {
                sum += water;
            }
        }
        System.out.println(sum);

    }
}