# comando para instalar o pyro4: pip install Pyro4
# comando para executar o daemon: python -m Pyro4.naming
import Pyro4


class Server(object): #Define a classe Server, que contém os métodos a serem expostos remotamente.
    @Pyro4.expose # Decorador que indica que o método welcomeMessage pode ser chamado remotamente.
    def welcomeMessage(self, name):
        return ("Olá bem vindo " + str(name))


def startServer(): # Define a função startServer, que configura e inicia o servidor.
    server = Server()
    daemon = Pyro4.Daemon() # Cria um Daemon do Pyro4, que é responsável por escutar chamadas remotas e gerenciar a comunicação.
    ns = Pyro4.locateNS() # Localiza o serviço de nomes (naming service) do Pyro4, que atua como um "DNS" para objetos remotos.
    uri = daemon.register(server) # Registra a instância server no Daemon, gerando um URI único para acesso remoto.

    ns.register("server", uri) #  Registra o URI do servidor no serviço de nomes com o alias "server".
    print("Ready. Object uri =", uri) # Exibe o URI do objeto registrado.
    daemon.requestLoop() # Inicia o loop de escuta do Daemon, aguardando chamadas remotas.


if __name__ == "__main__": # Verifica se o script está sendo executado diretamente (não importado) e chama startServer().
    startServer()
