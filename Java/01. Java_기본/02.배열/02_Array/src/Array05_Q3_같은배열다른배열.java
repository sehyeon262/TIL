// 두 개의 배열이 주어졌을 때 같은 배열이라면 “같습니다”, 다른 배열이라면 “다릅니다”를 출력하세요.

import java.util.Arrays;

public class Array05_Q3_같은배열다른배열 {
    public static void main(String[] args) {
        //1번 : 같습니다.
        int[] arr1 = {1,2,3,4,5};
        int[] arr2 = {1,2,3,4,5};
        
        if (Arrays.equals(arr1, arr2)) {
            System.out.println("같습니다");
        } else {
            System.out.println("다릅니다");
        }

        //2번 : 다릅니다.
        String[] arr3 = {"pig", "cow", "fish"};
        String[] arr4 = {"pig", "dog", "cat"};
        
        if (Arrays.equals(arr3, arr4)) {
            System.out.println("같습니다");
        } else {
            System.out.println("다릅니다");
        }
    }
}
