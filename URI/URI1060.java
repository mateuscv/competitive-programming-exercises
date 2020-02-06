import java.util.Scanner;

public class URI1060 {
    public static void main(String[] args) {
        int cont = 0;
        Scanner input = new Scanner(System.in);
        for (int i = 0; i < 6; i++){
            if (input.nextDouble() > 0){
                cont += 1;
            }
        }
        System.out.print(cont);
        System.out.print(" valores positivos\n");
    }
} 
