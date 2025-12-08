import java.util.Arrays;
public class array01_배열선언및생성 {
    public static void main(String[] args) throws Exception {
        // 배열을 선언
        int[] arr1;   // 권장
        int arr2[];   // 비권장

        // 배열을 초기화
        int[] arr3 = new int[10];
        String[] arr4 = new String[5];

        System.out.println(Arrays.toString(arr3));
        System.out.println(Arrays.toString(arr4));

        int[] arr5 = new int[] {1,2,3,4,5};
        System.out.println(Arrays.toString(arr5));
    }
}
