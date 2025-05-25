# Sistema Distribuído com Python PYRO

Este projeto foi desenvolvido para a disciplina de **Sistemas Distribuídos (CPD-032)** do semestre 2025.1, ministrada pelo professor Ernesto Massa.

## 1. Descrição da Tarefa

O objetivo do trabalho é a implementação de um sistema distribuído[cite: 1]. Conforme as especificações, o sistema deveria:
* Ser implementado em Java RMI, Python PYRO, ou Python gRPC, utilizando um "Name Server"[cite: 1].
* Apresentar a mesma funcionalidade de um sistema previamente desenvolvido com sockets[cite: 2].
* Como entregável, além dos arquivos fonte, deve ser produzido um pequeno vídeo de apresentação[cite: 3].
* O vídeo deve explicar as funcionalidades e comentar como o middleware escolhido foi utilizado na implementação[cite: 4].

Para este projeto, foi escolhida a tecnologia **Python PYRO**.

## 2. Funcionalidade

O sistema implementado consiste em uma aplicação cliente-servidor para processamento de mensagens. A interação ocorre da seguinte forma:

* O cliente solicita ao usuário que digite uma mensagem de texto (string).
* Essa mensagem é enviada para o servidor através de uma chamada de método remoto.
* O servidor recebe a mensagem e a processa, gerando três novas versões:
    1.  A string original convertida para letras **minúsculas**.
    2.  A string original convertida para letras **maiúsculas**.
    3.  A string original **invertida**.
* O servidor retorna um dicionário contendo as quatro versões da mensagem (original e as três processadas) para o cliente.
* O cliente exibe a resposta recebida no console.

## 3. Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Middleware:** Pyro5 (`Pyro5-5.13` ou superior)

## 4. Como Executar o Projeto

Para executar o sistema, é necessário ter o Python 3 e a biblioteca `Pyro5` instalados. A execução é dividida em três passos, cada um em um terminal diferente.

### Pré-requisitos

Instale a biblioteca `Pyro5` utilizando o pip:
```bash
pip install Pyro5
```

### Passo a Passo para Execução

**Passo 1: Iniciar o Name Server** 🌐

No primeiro terminal, inicie o serviço de nomes do PYRO. Ele é o responsável por permitir que o cliente encontre o servidor na rede.

```bash
python -m Pyro5.nameserver
```
> Deixe este terminal aberto durante toda a execução.

**Passo 2: Iniciar o Servidor do Projeto** 🖥️

No segundo terminal, navegue até a pasta do projeto e execute o script do servidor. Ele se registrará no Name Server e ficará aguardando por conexões.

```bash
python serverpyro.py
```
> A mensagem `Servidor Pyro5 pronto.` confirmará que ele está operando. Deixe este terminal aberto.

**Passo 3: Iniciar e Utilizar o Cliente** 🧑‍💻

No terceiro terminal, navegue até a pasta do projeto e execute o script do cliente.

```bash
python clientpyro.py
```
> O cliente se conectará ao servidor. Siga as instruções no console para:
> * Digitar uma mensagem para ser processada.
> * Digitar `sair` para encerrar o cliente.

## 5. Estrutura dos Arquivos

* `serverpyro.py`: Contém a lógica do servidor. É responsável por definir a classe `Processador` com seus métodos remotos, iniciar o daemon do PYRO e registrar o objeto no Name Server.
* `clientpyro.py`: Contém a lógica do cliente. É responsável por localizar o objeto remoto através do Name Server, criar um proxy para a comunicação e gerenciar a interação com o usuário.

## 6. Autor(es)
* [Rafael Queiroz Santos](mailto:rafaelqsantos33@gmail.com)
* [Brunna Gabriella de Moura da Silva](google.com.br)