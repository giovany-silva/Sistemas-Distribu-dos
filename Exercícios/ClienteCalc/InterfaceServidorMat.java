/* COM242 - SISTEMAS DISTRIBUIDOS 
   RMI - Exemplo de implementação. 
         Programa que utiliza funções remotas para realizar operacoes matemáticas.
   01/06/2021
*/

import java.rmi.*;

// Definição da interface que descreve os objetos remotos que poderao ser acessados pelo cliente
public interface InterfaceServidorMat extends Remote
{
    public double delta(double a, double b, double c) throws RemoteException;
    public double[] calcula(double a, double b,double c) throws RemoteException;

    
}