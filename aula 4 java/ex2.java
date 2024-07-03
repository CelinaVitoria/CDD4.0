package aula4;
import java.util.Scanner;
public class ex2 {

	public static void main(String[] args) {
		float nota[] = new float[5];
		 float media = 0, soma = 0;
		Scanner entrada = new Scanner(System.in);
		
		for (int x = 0; x< nota.length; x++) {
			System.out.println("Digite as notas dos alunos:");
			nota[x] = entrada.nextInt();
		}
		for (int x = 0; x< nota.length; x++) {
			soma = soma + nota[x];
		}
		media = soma/nota.length;
		System.out.println(media);
	}
}