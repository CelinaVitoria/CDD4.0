package aula4;

import java.util.Arrays;

public class ex3 {

	public static void main(String[] args) {
		int n[] = {81,32,17,8,20,91,43};
		int nI[] = new int[n.length];

		for (int x = 6; x > -1; x--) {
			System.out.print(n[x] + " ");
		}
		for (int y =0; y< n.length; y++) {
			nI[y] = n[6-y];
		}
		Arrays.sort(n);
		
		for (int x: n) {
			System.out.println(x +" ");
		}
	}
}