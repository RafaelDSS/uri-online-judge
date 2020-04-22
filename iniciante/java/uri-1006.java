import java.io.IOException;
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
        double a, b, c, mean;
        
        Scanner read = new Scanner(System.in);
        
        a = read.nextDouble();
        b = read.nextDouble();
        c = read.nextDouble();
        mean = ((a * 2.0) + (b * 3.0) + (c * 5.0)) / (2.0 + 3.0 + 5.0);
        
        System.out.printf("MEDIA = %.1f\n", mean);
    }
 
}