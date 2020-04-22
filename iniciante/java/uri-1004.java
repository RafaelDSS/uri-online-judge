import java.io.IOException;
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
        int a, b, prod;
        
        Scanner read = new Scanner(System.in);
        
        a = read.nextInt();
        b = read.nextInt();
        prod = a * b;
        
        System.out.println("PROD = " + prod);
    }
 
}