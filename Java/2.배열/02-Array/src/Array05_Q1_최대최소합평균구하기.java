public class Array05_Q1_최대최소합평균구하기 {
    public static void main(String[] args) {
        int[] nums = {64, 53, 123, 23, 444, 98, 12};

        // 최대값 세팅 방법
        int max = 0;
        // int max2 = Integer.MIN_VALUE;
        // int max3 = nums[0];
        int min = nums[0];
        int sum = 0;

        for (int i = 0; i < nums.length; i++) {
            
            // 최소값 찾기
            if (min > nums[i]) {
                min = nums[i];
            }
            
            // 최대값 찾기
            if (max < nums[i]) {
                max = nums[i];
            }

            // 합계 누적
            sum += nums[i];
        }
        // 평균 계산
        double avg = (double) sum / nums.length;

        System.out.println("최소값: " + min);
        System.out.println("최대값: " + max);
        System.out.println("합계: " + sum);
        System.out.println("평균: " + avg);
    }
}
