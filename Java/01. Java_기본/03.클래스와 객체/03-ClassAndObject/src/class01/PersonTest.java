package class01;

public class PersonTest {
    public static void main(String[] args) {
        // 사람의 정보를 관리하자!

        String name1 = "Kim";
        int age1 = 24;
        String hobby1 = "Youtube";

        String name2 = "Park";
        int age2 = 25;
        String hobby2 = "Blog";

        // 사람이 100명이라면... 너무 힘들다!!

        // 배열 사용!
        int size = 100;
        String[] names = new String[size];
        int[] ages = new int[size];
        String[] hobbies = new String[size];

        names[0] = "Kim";
        names[1] = "Park";
        ages[0] = 24;
        ages[1] = 25;
        hobbies[0] = "Youtube";
        hobbies[1] = "Blog";
    }
}
