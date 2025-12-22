package class03;

public class PersonTest {
    public static void main(String[] args) {
        // Yang을 생성해보자!
        // 클래스이름 변수이름 = new 클래스이름();
        Person kim = new Person(); 
        kim.name = "Kim";
        kim.age = 24;
        kim.hobby = "Youtube";

    
        Person park = new Person();
        park.name = "Park";
        park.age = 25;
        park.hobby = "Blog";

        // 클래스 함수 사용
        // kim.info();
        // park.info();

        // 아래에 작성된 200을 인자
        kim.study(100);

    }

}
