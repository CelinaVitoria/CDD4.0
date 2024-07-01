package basico3;

public class ex7 {

	public static void main(String[] args) {
		double soma = 0;
		int soma3=0,soma5=0,somaTotal=0;
		for(int x=1; x<20;x++) {
			int mult3 = x * 3;
			int mult5 = x * 5;
			soma3 = soma3 + mult3;
			soma5 = soma5 + mult5;
			}
		somaTotal = soma3 + soma5;
		System.out.println(soma3);
		System.out.println(soma5);
		System.out.println(somaTotal);
		}

	}

