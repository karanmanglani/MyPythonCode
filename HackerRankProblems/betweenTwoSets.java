import java.util.*;

public class Solution {
    public static int gcd(int a, int b) {
        while (a > 0 && b > 0) {
            
            if (a >= b) {
                a = a % b;
            }
            else {
                b = b % a;
            }
        }

        return a + b;
    }

    public static int lcm(int a, int b) {
        return (a / gcd(a, b)) * b;
    }
    
    public static int getTotalX(int[] a, int[] b) {
        
        int multiple = 0;
        for(int i : b) {
            multiple = gcd(multiple, i);
        }
//        System.err.println("Multiple: " + multiple);
        
        int factor = 1;
        for(int i : a) {
            factor = lcm(factor, i);
            if (factor > multiple) {
                return 0;
            }
        }

        if (multiple % factor != 0) {
            return 0;
        }
//        System.err.println("Factor: " + factor);
        
        int value = multiple / factor;
        
        int max = Math.max(factor, value);
        int totalX = 1;
        
        for (int i = factor; i < multiple; i++) {
            if (multiple % i == 0 && i % factor == 0) {
                totalX++;
            }
        }

        return totalX;
        
    }
    
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m = scan.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = scan.nextInt();
        }
        int[] b = new int[m];
        for (int i = 0; i < m; i++) {
            b[i] = scan.nextInt();
        }
        scan.close();
        
        int total = getTotalX(a, b);
        System.out.println(total);
    }
}