import java.util.Scanner;
import java.util.Arrays;

public class 브론즈_10809_알파벳찾기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        
        int[] pos = new int[26];
        Arrays.fill(pos, -1);  // 전부 1로 초기화!
        
        for (int i = 0; i < str.length(); i++) {
            int idx = str.charAt(i) - 'a';
            
            // 처음 등장했을 때만 저장
            if (pos[idx] == -1) {
                pos[idx] = i;
            }
        }

        for (int i = 0; i < 26; i++) {
            System.out.print(pos[i] + " ");
        }
        
    }
}
