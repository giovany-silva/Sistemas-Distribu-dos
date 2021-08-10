/* COM242 - SISTEMAS DISTRIBUIDOS 
   RMI - Cálculo da equação quadrática. 
         Programa que utiliza funções remotas para realizar operacoes matemáticas.
   01/06/2021
*/

import java.rmi.*;
import java.util.Scanner;
import javafx.util.Pair;

public class Cliente
{
	public Cliente()
	{
		System.out.println("Executando Cliente... \n");
		try
		{   // Acessa o servidor de nomes para localização das funções remotas
			msi = (InterfaceServidorMat) Naming.lookup("rmi://192.168.0.18/ServidorMat_1");
      
		}
		catch (Exception e)
		{
			System.out.println("Falhou a execucao do Cliente.\n"+e);				
			System.out.println("Certifique se a aplicacao no servidor esta em execucao.\n");				
			System.exit(0);
		}
	}
	
	public static void main (String[] argv)
	{
		Cliente c = new Cliente();
		Scanner keyboard = new Scanner(System.in);
		System.out.println("Entre com os coeficientes a, b e c separados por espaco:");
		double A = keyboard.nextDouble();
		double B = keyboard.nextDouble();
    double C = keyboard.nextDouble();
		System.out.println("");
		
		try
		{   // Cada chamada de uma função remota é uma instância da classe Cliente
      double raizes[] = c.calcula(A, B, C);
    
      System.out.println("X'= "+ raizes[0]);
      System.out.println("X''= "+ raizes[1]);
	}
		catch (Exception e)
		{
			System.out.println("Excepção durante chamadas remotas:" +e);
		}
	}

	private InterfaceServidorMat msi; // A interface para o objecto remoto
	
	
	// Chamada as funções remotas para realização das operações matemáticas
	public double[] calcula(double A, double B, double C) throws RemoteException{
		 return msi.calcula(A, B, C);
	}

	
}