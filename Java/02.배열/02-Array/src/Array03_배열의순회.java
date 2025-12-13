import java.util.Arrays;

public class Array03_배열의순회 {
    public static void main(String[] args) {
        int[] intArray = {1, 3, 5, 7, 9};

        for (int i = 0; i < intArray.length; i++) {
            System.out.println(intArray[i]); // 한 줄에 하나씩 출력
            // System.out.print(intArray[i]);  // 한줄에 다 출력
        }

        // for-each 문
        // for(요소 : 반복할 것)
        
        // read only
        for(int x : intArray) {
            // System.out.println(x);
            x *= 2;
        }
        System.out.println(Arrays.toString(intArray));  // [1, 3, 5, 7, 9] => 2배 아님!
    }
}