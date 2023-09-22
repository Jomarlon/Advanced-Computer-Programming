import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] names = new String[20];

        for (int i = 0; i < 20; i++) {
            System.out.print("Name #" + (i + 1) + ": ");
            names[i] = scanner.nextLine();

        }
        Arrays.sort(names);

        System.out.println("Sorted Names: ");
        for (int i = 0; i < 20; i++) {
            System.out.println(names[i]);
        }

    }
}
