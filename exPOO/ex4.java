package exPOO;

import java.util.Scanner;

public class ex4 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.print("Digite um texto:");
		String texto = entrada.nextLine();
		String resultado = texto.toUpperCase();
		System.out.println(resultado);

	}
}
