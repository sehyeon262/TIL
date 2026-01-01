
import java.util.Random;

// 싸피생의 하루 일과
/* 
System.out.println("아침에 일어난다.");
System.out.println("교육장으로 대중교통을 이용하여 이동한다.");
System.out.println("오전 수업(Live)을 듣는다.");
System.out.println("점심을 먹는다.");
System.out.println("오후 수업(실습)을 진행한다.");
System.out.println("집으로 대중교통을 이용하여 이동한다.");
System.out.println("과제를 해결한다.");
System.out.println("잠을 잔다.");
*/

 public class SsafyRoutine {
    public static void main(String[] args) {
        System.out.println("아침에 일어난다.");
        이동("교육장", "셔틀버스");
        // boolean 과제 = 교육();  
        이동("집", "지하철");
        
        // if (과제 == true)
        // if (과제)
        if (교육()) {
            System.out.println("과제를 해결한다.");
        }
        System.out.println("잠을 잔다.");
    }

    // 함수
    // - 관련된 문장들을 하나로 묶은 것 (이름을 붙인 것)
    // - 실행 가능한 단위
    // - 변수명 한글로 쓰는 거 권장 X => 영어로 쓰기를 권장!!!

    // public static void 교육() {
    //     System.out.println("오전 수업(Live)을 듣는다.");
    //     System.out.println("점심을 먹는다.");
    //     System.out.println("오후 수업(실습)을 진행한다.");
    // }

    // 반환값
    public static boolean 교육() {
        System.out.println("오전 수업(Live)을 듣는다.");
        System.out.println("점심을 먹는다.");
        System.out.println("오후 수업(실습)을 진행한다.");
        // 랜덤에따라 true 또는 false 반환
        return new Random().nextBoolean();
    }

    public static void 이동(String 장소, String 교통수단) {
        System.out.println(장소 + "으로 " + 교통수단 + "를(을) 이용하여 이동한다.");
    }
    
}
