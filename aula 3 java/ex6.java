package basico3;

import java.util.Scanner;

public class ex6 {

	public static void main(String[] args) {
		int alunos = 0;
		double nota = 0, media = 0, soma = 0;
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite o nmr de alunos na sala:");
		alunos = entrada.nextInt();
		int qtd = alunos;
		for (int x = 0; x < alunos; x++) {
				System.out.println("Digite a nota:");
				nota = entrada.nextDouble();
				soma += nota;
			}
			media = soma/qtd;
			System.out.println(media);
			entrada.close();

	}

}
