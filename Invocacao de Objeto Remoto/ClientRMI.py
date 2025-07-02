import Pyro4

name = input("Escreva qualquer palavra ").strip() # Solicita que o usuário digite uma palavra e armazena o valor em name (removendo espaços extras com strip()).
server = Pyro4.Proxy("PYRONAME:server") # Cria um proxy (representação local) do objeto remoto registrado como "server" no serviço de nomes.
# Indica que o objeto é identificado pelo nome "server" no naming service.
print(server.welcomeMessage(name)) # Chama o método remoto welcomeMessage no servidor, passando name como argumento.
# Imprime a resposta retornada pelo servidor (ex.: "Olá bem vindo [nome]").
