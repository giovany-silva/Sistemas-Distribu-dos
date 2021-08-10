/* COM242 - SISTEMAS DISTRIBUIDOS 
   RMI - Cálculo da equação quadrática. 
         Programa que utiliza funções remotas para realizar operacoes matemáticas.
   01/06/2021
*/

import java.rmi.*;
import java.rmi.server.*;
import java.lang.Math;


// Classe no servidor que implementa os métodos remotos
public class ServidorMat extends UnicastRemoteObject implements InterfaceServidorMat
{
    public ServidorMat() throws RemoteException
    {
        System.out.println("Novo Servidor instanciado...");
    }
	
    public double delta(double a, double b, double c) throws RemoteException
    {
        System.out.println("Cliente digitou os seguintes valores: a = " + a + ", b = " + b + " e c =" + c);
         
	return b*b-4*a*c;
    }
	
    public double[] calcula(double a, double b,double c) throws RemoteException
    {
        double solucao[] = new double[2];
        System.out.println("Valores recebidos do cliente: x = " + a + "  y = " + b+ " "+c);
        double Delta = delta(a, b, c);
        
        solucao[0] = (-b -(java.lang.Math.sqrt(Delta))) /( 2 * a);
        solucao[1] = (-b +(java.lang.Math.sqrt(Delta))) / (2 * a);
        
	return solucao;
    }
	
    
} 