package construtor;

public class Carro {
	public String cor;
	public double preco;
	public String modelo;
	public Carro() {
	}
	public Carro(String cor) {
		this.cor=cor;
	}
	public Carro(String cor, double preco) {
		this.cor=cor;
		this.preco=preco;
	}
	boolean acao = false;
	public void ligar() {
		if (acao == false) {
		System.out.println("ligado");	
		}
		else if(acao == true) {
			System.out.println("já está ligado");	
		}
	}
	public void desligar() {
		if(acao  == false) {
			System.out.println("desligado");
			}
		else if (acao == true) {
			System.out.println("já está desligado");
		}
	}
	public void JáEstáLigado() {
		if(acao == false) {
			System.out.println("Já está ligado");
			}

	}
}
