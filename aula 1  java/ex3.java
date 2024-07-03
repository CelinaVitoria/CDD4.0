package basico1;

import java.util.Scanner;

public class ex3 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um numero:");
		double resp = entrada.nextDouble();
		Scanner entrada2 = new Scanner(System.in);
		System.out.println("Digite um numero:");
		double resp2 = entrada2.nextDouble();
		Scanner entrada3 = new Scanner(System.in);
		System.out.println("Digite um numero:");
		double resp3 = entrada3.nextDouble();
	
		if (resp > resp2 && resp > resp3) {
			System.out.printf("%f resp é o maior %n", resp);
		}
		if (resp2 > resp && resp2 > resp3) {
			System.out.printf("%f resp2 é o maior %n", resp2);
		}
		else {
			System.out.printf("%f resp3 é o maior %n", resp3);
		}
	}
}
