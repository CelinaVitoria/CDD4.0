package exPOO;

import java.util.Scanner;
import java.util.StringTokenizer;

public class ex2 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.print("Digite uma frase:");
		String texto = entrada.nextLine();
		StringTokenizer exemplo = new StringTokenizer(texto);
		System.out.println(exemplo.countTokens());
		entrada.close();
	}

}
