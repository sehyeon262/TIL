import java.util.Scanner;
public class 브론즈_1546_평균 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        double[] arr = new double[n];
        double max = 0;

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            if (max < arr[i]) {
                max = arr[i];
            }
        }
        
        double sum = 0;
        for (int j = 0; j < n; j++) {
            arr[j] = arr[j] / max * 100;
            sum += arr[j];
        }

        double avg = sum / n;
        System.out.println(avg);
    }
}
