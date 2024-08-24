# Sistema de Pagamento com Pix e WebSockets

Este projeto é uma demonstração simples de como criar um sistema de pagamento
com Pix utilizando WebSockets. O projeto é composto por uma API em Flask que
cria um pagamento, envia os dados do pagamento para o cliente (que é uma página
HTML simples), e então espera que o cliente confirme o pagamento. Quando o
cliente confirma o pagamento, o servidor emite um evento para o cliente com a
confirmação do pagamento.

O projeto utiliza as seguintes tecnologias:

- Flask
- Flask-SQLAlchemy
- Flask-SocketIO
- qrcode
- pillow

## Instalação

Para instalar o projeto, execute o seguinte comando:

    pip install -r requirements.txt

## Execução

Para executar o projeto, execute o seguinte comando:

    python app.py

## Uso

Abra um navegador e acesse a URL http://localhost:5000. O projeto irá gerar um
novo pagamento e mostrar o QRCode do pagamento. Confirme o pagamento e o
projeto irá mostrar uma mensagem de confirmação do pagamento.

## Contribui o

Este projeto uma demonstra o de como criar um sistema de pagamento com
Pix e WebSockets. O projeto livre para uso e contribui o. Caso tenha
alguma dica ou sugestão , por favor, abra um pull request.
