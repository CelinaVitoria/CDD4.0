package exPOO;

public class ex6 {

	public static void main(String[] args) {
		String caracteres[] = {"a","vida","é","bela"};
		for(int i = caracteres.length-1; i >= 0; i--) {
			String texto = caracteres[i].toUpperCase();
			System.out.println(texto + " ");
		}
	}

}
