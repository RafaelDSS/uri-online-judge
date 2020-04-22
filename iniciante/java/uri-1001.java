import java.io.IOException;
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
        int a, b, x;
        
        Scanner read = new Scanner(System.in);
        
        a = read.nextInt();
        b = read.nextInt();
        x = a + b;
        
        System.out.println("X = " + x);
    }
 
}