import Pyro5.api
import Pyro5.server

"""
    Antes de iniciar o servidor, certifique-se de que o NameServer do Pyro5 esteja rodando e configurado corretamente.
    Para iniciar o Nameserver, execute o comando "python -m Pyro5.nameserver" em um terminal dedicado.
"""


"""
    Funcao para processar a mensagem do usuario e retorna-la em maiuscula, minuscula e reversa.
    Há feedback da mensagem recebida e a processada no console para outras implementações de logica de negocios.
"""
@Pyro5.api.expose
class Processador:
    def process_mensagem(self, mensagem):
        print(f"Recebido: {mensagem}")
        minuscula = mensagem.lower()
        maiuscula = mensagem.upper()
        reversa = mensagem[::-1]

        resposta = {
            "original": mensagem,
            "minuscula": minuscula,
            "maiuscula": maiuscula,
            "reversa": reversa
            
        }
        print(f"Processado: {resposta}")
        return resposta

"""
    Funcao principal do servidor Pyro5.
    Registra o servidor no NameServer do Pyro5 e inicia o loop de requisicoes.
    Cria o daemon que escuta conexoes de clientes e expoe objetos. Localiza o Nameserver e permite registros nele.
    Registra a funcao de processamento no daemon que retorna um URI e registra o example.processador no Nameserver associado ao URI, 
    permitindo que clientes se conectem ao servidor.
"""

def main():
    daemon = Pyro5.server.Daemon()
    ns = Pyro5.api.locate_ns()
    uri = daemon.register(Processador)
    ns.register("example.processador", uri)

    print("Servidor Pyro5 pronto.")
    daemon.requestLoop()


if __name__ == "__main__":
    main()
