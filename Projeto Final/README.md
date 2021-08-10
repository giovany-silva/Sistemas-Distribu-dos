Este diretório contém a solução para o problema de automatização de divulgação de recomendações de ações em uma corretora. Para isso,
utilizamos o RabbitMQ na versão 3.8.16 e a Linguagem Python 3.8. A lógica da Solução pode ser observada a seguir:

* Pastas clientes: possuem um arquivo Python(manipula as inscrições em tópicos) e um arquivo txt(guarda as preferências do cliente).

* arquivo broker.py: código que atua como broker RabbitMQ, esse arquivo consulta o Banco de Dados PostgreSQL para recomendar para os inscritores

* Interface_analista.py: código que atua como interface do analista, esse código faz a conexão da interface com o Banco PostgreSQL para que seja
possível a divulgação de ofertas.