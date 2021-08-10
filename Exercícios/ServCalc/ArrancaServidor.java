/* COM242 - SISTEMAS DISTRIBUIDOS 
   RMI - Exemplo de implementação. 
         Programa que utiliza funções remotas para realizar operacoes matemáticas.
   14/04/2020
*/

import java.rmi.*;
import java.net.*;
import java.rmi.registry.Registry;

// Classe que registra o servidor da aplicação junto ao servidor de nomes
public class ArrancaServidor
{
    public static void main(String argv[])
    {
        try
        {
			System.out.println("Subindo servidor...");
			InetAddress IP = InetAddress.getLocalHost();
            System.setProperty("java.rmi.server.hostname", IP.getHostAddress());
			Registry r = java.rmi.registry.LocateRegistry.createRegistry(1099); // Registra a porta da aplicação
            Naming.rebind("ServidorMat_1", new ServidorMat()); // Associa o servidor a um nome para o acesso do cliente
        }
        catch (Exception e)
        {
            System.out.println("Ocorreu um problema no arranque do servidor.\n"+e.toString());
        }
    }
}