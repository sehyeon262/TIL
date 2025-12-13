// 0 ~ 9 까지의 값으로만 이루어져 있는 배열이 주어졌을 때, 
// 각각의 0 ~ 9까지의 값이 몇 번 등장하였는지를 출력하세요. (단, 한 번도 등장하지 않은 숫자는 출력하지 않습니다.)

public class Array05_Q2_빈도수구하기 {
    public static void main(String[] args) {
        int[] intArray = {3, 7, 2, 5, 7, 7, 9, 2, 8, 1, 1, 5, 3};

        // 0~9까지의 빈도를 저장할 배열
        int[] count = new int[10];

        // intArray의 값들 등장 횟수 세기
        for (int i = 0; i < intArray.length; i++) {
            int value = intArray[i];
            count[value]++;
        }
        
        // 등장한 숫자만 출력
        for (int i = 0; i < count.length; i++) {
            if (count[i] > 0) {
                System.out.println(i + " : " + count[i] + "번");
            }
        }
    }

}
