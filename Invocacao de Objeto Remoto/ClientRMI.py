import Pyro4

name = input("Escreva qualquer palavra ").strip()
server = Pyro4.Proxy("PYRONAME:server")
print(server.welcomeMessage(name))
