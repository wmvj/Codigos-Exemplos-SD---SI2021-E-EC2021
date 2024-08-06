import rpyc


class MyService(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_add_numbers(self, x, y):
        return x+y


if __name__ == "__main__":
    from rpyc.utils.server import ThreadPoolServer
    server = ThreadPoolServer(MyService, port=12345)
    server.start()

# Tipos de servidor
# - OneShotServer (Servidor vai atender um cliente por vez e depois termina)
# - ForkingServer (Servidor atende varios cliente que se conecta a ele e dispara  um processo novo para cada cliente)
# - ThreadedServer (Servidor atende varios clientes que se conecta a ele e dispara uma nova thread para cada cliente)
# - ThreadPoolServer (Servidor atende varios clientes e gerencia um conjunto de threads)
