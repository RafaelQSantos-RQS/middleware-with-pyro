# client_pyro.py

import Pyro5.api

"""   
    Cliente Pyro5 que procura e se conecta ao servidor NameServer do Pyro5.
    O cliente envia mensagens ao servidor e recebe como resposta do servidor a sua propia mensagem.
    Permite ao cliente também sair do programa ao digitar sair no console.
"""

def main():
    ns = Pyro5.api.locate_ns()
    uri = ns.lookup("example.processador")
    proxy = Pyro5.api.Proxy(uri)

    print("[INFO] Conectado ao servidor Pyro5.")

    while True:
        mensagem = input("Digite uma mensagem (ou 'sair' para encerrar): ")

        if mensagem.lower() == 'sair':
            print("Encerrando cliente.")
            break

        resposta = proxy.process_mensagem(mensagem)

        print(f"\nResposta do servidor:")
        print(f"Original: {resposta['original']}")
        print(f"Minuscula: {resposta['minuscula']}")
        print(f"Maiuscula: {resposta['maiuscula']}")
        print(f"Reversa: {resposta['reversa']}\n")


if __name__ == "__main__":
    main()
