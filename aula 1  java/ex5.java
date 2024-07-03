package basico1;

import java.util.Scanner;

public class ex5 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite a nota1:");
		float nota = entrada.nextFloat();
		Scanner entrada2 = new Scanner(System.in);
		System.out.println("Digite a nota2:");
		float nota2 = entrada.nextFloat();
		float media = (nota + nota2)/2;
			System.out.println(media);
	}

}
