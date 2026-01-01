package class02;

public class PersonTest {
    public static void main(String[] args) {
        // Yang을 생성해보자!
        // 클래스이름 변수이름 = new 클래스이름();
        Person kim = new Person(); 
        kim.name = "Kim";
        kim.age = 24;
        kim.hobby = "Youtube";

        System.out.printf("나의 이름은 %s입니다. %n나이는 %d세, 취미는 %s입니다.%n", kim.name, kim.age, kim.hobby);

        Person park = new Person();
        park.name = "Park";
        park.age = 25;
        park.hobby = "Blog";

        System.out.printf("나의 이름은 %s입니다. %n나이는 %d세, 취미는 %s입니다.%n", park.name, park.age, park.hobby);

        // 함수 사용!
        System.out.println("=======함수 사용=======");
        info(kim.name, kim.age, kim.hobby);
        info(park.name, park.age, park.hobby);
    }

    public static void info(String name, int age, String hobby) {
        System.out.printf("나의 이름은 %s입니다. %n나이는 %d세, 취미는 %s입니다.%n", name, age, hobby);
    }
}
