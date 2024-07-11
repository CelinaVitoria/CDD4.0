package JavaPOO2;

public class ClassePessoa {
		String nome, acao = " ";
		public void comer() {
			if (acao.equals(" ")) {
			System.out.println(nome + " está comendo");	
			acao = "comendo";
		}else if(acao.equals("dormindo")) {
				System.out.println(nome + " está dormindo, nao pode comer");
			}else if(acao.equals("andando")) {
					System.out.println(nome + " está andando, nao pode comer");
				}
		}
		public void parardecomer() {
			if(acao.equals("comendo")) {
				System.out.println(nome + " parou de comer");
				acao = " ";}
				else  if (acao.equals(" ")) {
					System.out.println(nome + " n ta comendo, n pode parar de comer");
					}else  if (acao.equals("dormindo")) {
					System.out.println(nome + " esta dormindo, n pode parar de comer");
					}else  if (acao.equals("andando")) {
					System.out.println(nome + " esta andando, n pode parar de comer");
					}
		}
		public void dormir() {
			if (acao.equals(" ")) {
				System.out.println(nome + " está dormindo");	
				acao = "dormindo";
			}else if(acao.equals("comendo")) {
					System.out.println(nome + " está comendo, dormir");
				}else if(acao.equals("andando")) {
						System.out.println(nome + " está andando, nao pode dormir");
					}
		}
		public void parardedormir() {
			if(acao.equals("dormindo")) {
				System.out.println(nome + " parou de dormir");
				acao = " "; }
				else if (acao.equals(" ")) {
					System.out.println(nome + " n ta dormindo, n pode parar de dormir");
					}else if (acao.equals("comendo")) {
					System.out.println(nome + " esta comendo, n pode parar de dormir");
					}else if (acao.equals("andando")) {
					System.out.println(nome + " esta andando, n pode parar de dormir");
					}
				}
				
		public void andar() {
			if (acao.equals(" ")) {
				System.out.println(nome + " está andando");	
				acao = "andando";
			}else if(acao.equals("dormindo")) {
					System.out.println(nome + " está dormindo, nao pode andar");
						}else if(acao.equals("comendo")) {
						System.out.println(nome + " está comendo, nao pode andar");
						}
				}
		public void parardeandar() {
			if(acao.equals("andando")) {
				System.out.println(nome + " parou de andar");
				acao = " ";}
				else if (acao.equals(" ")) {
					System.out.println(nome + " n ta andando, n pode parar de andar");
					}else if (acao.equals("comendo")) {
					System.out.println(nome + " esta comendo, n pode parar de andar");
					}else if (acao.equals("andando")) {
					System.out.println(nome + " esta andando, n pode parar de andar");
					}
				}
				}
