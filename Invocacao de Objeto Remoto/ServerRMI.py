# comando para isntalar o pyro4: pip install Pyro4
# comando para executgar o daemon: python -m Pyro4.naming
import Pyro4


class Server(object):
    @Pyro4.expose
    def welcomeMessage(self, name):
        return ("Olá bem vindo " + str(name))


def startServer():
    server = Server()
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(server)

    ns.register("server", uri)
    print("Ready. Object uri =", uri)
    daemon.requestLoop()


if __name__ == "__main__":
    startServer()
