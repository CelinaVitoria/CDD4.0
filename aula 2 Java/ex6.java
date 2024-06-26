package basico1;
import java.util.Scanner;
public class ex6 {

	public static void main(String[] args) {
		char opcao;
		Scanner input = new Scanner(System.in);
		System.out.println("Digite F para feminino e M para masculino:");
		opcao = input.next().charAt(0);
		if (opcao == 'F') {
			System.out.println("Feminino");}
		else {
			System.out.println("Masculino");}
	}
}
