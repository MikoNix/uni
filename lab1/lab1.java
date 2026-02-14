import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Напряжение: ");
        int u = scanner.nextInt();

        System.out.print("Сопротивление: ");
        int r = scanner.nextInt();

        double current = (double) u / r;
        System.out.println("Сила тока: " + current);
    }
}
