package aula4;
import java.util.Scanner;
public class ex1 {

	public static void main(String[] args) {
		int a[] = new int[10];
		int b[] = new int[10];
		int c[] = new int[10];
		int d[] = new int[10];
		Scanner entrada = new Scanner(System.in);
		
		for (int x = 0; x< a.length; x++) {
			System.out.println("Digite os valores do array a:");
			a[x] = entrada.nextInt();
		}
		for (int x = 0; x< b.length; x++) {
			System.out.println("Digite os valores do array b:");
			b[x] = entrada.nextInt();
		}
		for (int x = 0; x< c.length; x++) {
			System.out.println("Digite os valores do array c:");
			c[x] = entrada.nextInt();
		}
		for (int x = 0; x< d.length; x++) {
			System.out.println("Digite os valores do array d:");
			d[x] = entrada.nextInt();
		}
		for(int y : a) {
		System.out.println(y + " ");
		}
		for(int y : b) {
			System.out.println(y + " ");
			}
		for(int y : c) {
			System.out.println(y + " ");
			}
		for(int y : d) {
			System.out.println(y + " ");
			}
	}
}