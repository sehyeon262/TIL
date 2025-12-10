public class Array99_PrintTest {
    public static void main(String[] args) {

        // print를 써보자
        System.out.print("Hello World");
        System.out.print("Hello World\n");

        // \n을 사용하면 줄이 바뀐다.
        System.out.println("Hello World!!!");
        System.out.println("Hello World!!!");

        // System.out.println("\");
        System.out.println("\\");
        System.out.println("\\\\");

        // escape sequence : 특정한 문자 조합은 문자 그대로가 아니라 다른 의미를 갖는다.
        // ex) \n \\ \t

        System.out.printf("%d\n", 10); // 정수 (10진수) -> 10
        System.out.printf("%o\n", 10); // 정수 (8진수) -> 12
        System.out.printf("%x\n", 10); // 정수 (16진수) 소문자 -> a
        System.out.printf("%X\n", 10); // 정수 (16진수) 대문자 -> A

        System.out.printf("%d\n", 10); // 4칸을 확보한 뒤 오른쪽부터 차지 -> 10
        System.out.printf("%-4d\n", 10); // 4칸을 확보한 뒤 왼쪽부터 차지 -> 10
        System.out.printf("%04d\n", 10); // 4칸을 확보한 뒤 오른쪽부터 차지 (빈칸은 0으로 채움) -> 0010

        System.out.printf("%f\n", 10.12345); // 실수  -> 10.123450
        System.out.printf("%.2f\n", 10.12345); // 실수 (소수점 둘째자리까지) - 10.12345로 바꿔서 반올림됨 -> 10.12
        // 자동으로 반올림해준다.

        System.out.printf("%s\n", "사과"); // 문자열 -> 사과
        System.out.printf("%c\n", 'A'); // 문자 -> A
        System.out.printf("%d\n", (int) 'A'); // 문자를 정수로 출력 -> 65
    }
}