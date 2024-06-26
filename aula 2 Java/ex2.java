package basico1;
import java.util.Scanner;
public class ex2 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um numero:");
		double resp = entrada.nextInt();
		if (resp >= 0) {
			System.out.println("positivo");
		}
		else {
			System.out.println("negativo");
		}
	}

}
