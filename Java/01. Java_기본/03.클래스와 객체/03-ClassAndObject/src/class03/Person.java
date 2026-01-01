package class03;

public class Person {
    // 데이터
    // 데이터 필드를 초기화 하지 않으면 -> 기본값이 들어가있음
    String name;
    int age;
    String hobby;

    // 기능 (매개변수 X)
    void info() {
        System.out.printf("나의 이름은 %s입니다. %n나이는 %d세, 취미는 %s입니다.%n", name, age, hobby);
    }

    // 기능 (매개변수 O)
    void study(int time) {
        //int time = ?
        //파라미터는 해당 위치에 선언한 지역변수
        System.out.println(time + "시간만큼 공부를 했습니다.");
    }

    // 메서드 오버로당
    // 이름이 같으면서, 매개변수가 다른 메서드 (파라민터의 타입, 개수, 순서가 달라야함)
    void study(long time) {

    }

    void study(double time) {

    }

    // (int, int) 같음 => 에러 남!!
    /* 
    void study(int time1, int time2) {
        
    }
    void study(int time2, int time1) {
    
    }
    */

    // 순서가 다름 => 에러 안남!! (String, int) != (int, String)
    void study(String str, int time) {

    }
    void study(int time, String str) {

    }
}
