import java.io.IOException;
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
        double a, b, mean;
        
        Scanner read = new Scanner(System.in);
        
        a = read.nextDouble();
        b = read.nextDouble();
        mean = ((a * 3.5) + (b * 7.5)) / (3.5 + 7.5);
        
        System.out.printf("MEDIA = %.5f\n", mean);
    }
 
}