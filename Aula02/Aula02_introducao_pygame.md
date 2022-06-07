# Curso PyGame

## Introdução ao Pygame - Jogo Pong

Crie um projeto na sua IDE PyCharm chamado Pong.

No arquivo main.py vamos importar nossa biblioteca PyGame para conseguir desenvolver nosso primeiro jogo.

Digite o Import pygame e você perceberá que o pygame ficou grifado em vermelho pois não temos a biblioteca instalada em nosso ambiente de desenvolvimento.

Para instalarmos o PyGame clique sobre o import pygame e vcocê perceberá que irá aparecer uma lampada (dica) na cor vermelha. Clique sobre a dica e escolha a opção "Install Package PyGame" e a IDE irá instala-la em seu ambiente virtual.

![Instalando PyGame](img/img01.jpg)

Uma vez instalado o Pygame podemos iniciar a configuração de janela de nosso game. Digite o código como abaixo:

![Inicializando PyGame](img/img02.jpg)

Na linha 4 temos a inicialização da biblioteca do pygame. Na linha 6 definimos o tamanho da janela de execução de nosso game e na linha 8 definimos o texto da barra de titulo desta janela.

Se você mandar executar o projeto neste momento vai perceber que a janela irá apenas piscar na sua tela, ou seja a janela é executada e logo em seguida a execução é encerrada.

Para resolvermos esse problema temos que criar um laço com um loop de condição infinita. Todo jogo possui um laço deste modo "While True".

Na próxima imagem vamos definir uma variavel executa valendo True que será passada para o nosso laço While mantendo a janela do jogo em execução permanente.

![Criando loop](img/img03.jpg)

Na linha 12 criamos a variável executa= True e passamos ela como condição do laço While. Assim nosso jogo ficará com a janela sendo atualizada de forma permanente pela linha de código 19.

Para encerrarmos a execução devemos alterar o valor da variável executa para False terminando nosso laço. 

Para isso o usuário deverá clicar no botão "X" de nossa janela e dentro de nosso programa esse clique constitui um evento que deve-se captura e tratado em nosso código.

Na linha 14 é montado um laço for que percorre uma lista de eventos gerado pelo comando pygame.event.get() que consegue capturar o pressionamento de teclas ou cliques do mouse para podermos tratr-los de maneira adequada ao jogo.

Assim na linha 16 vamos verificar no IF se temos um evento do tipo QUIT e se sim alteramos o conteudo da variável executa para False encerrando nosso game.

## Colocando Imagem de Fundo em nosso Jogo

Observe na próxima imagem as linhas grifadas em azul. 
Na linha 10 importamos a imagem de fundo de nosso jogo utilizando o pygame.image.load.
Essa imagem pode ser obtida junto com um aquivo zip com recursos necessários ao nosso projeto junto com esse tutorial.

Baixe o arquivo zip e descompacte a pasta "assets" que está compactada neste arquivo dentro da pasta do seu projeto do Pycharm para que o projeto possa ter acesso as imagens que utilizaremos.

Geralmente a pasta PyCharm Projects está em C:\Usuarios \ "nome do usuario" \ ...

Na linha 12 posicionamos a imagem pelo seu canto superior direito na posição superior direito da janela de nosso jogo.

![background](img/img04.jpg)

Após inserida a imagem corretamente executamos nosso projeto para verificarmos o resultado.

![background resultado](img/img05.jpg)

## Inserindo Jogadores e a bola ao Game

Vamos agora posicionar a imagem dos jogadores 1 e 2 em frente as suas metas (linhas de defesa) e a bola centralizada no centro de nosso campo de jogo.

Nas linhas14 e 16 temos o código de importação da imagem de cada um dos jogadores e nas linhas 15 e 17 podemos observar os códigos que posicionam as imagens dos jogades nas metas.

O mesmo acontece com a bola na linha 19 imprtamos a imagem da bola e na linha 20 a posicionamos no centro do campo de jogo.

Digite os códigos conforme a imagem abaixo.

![jogadores e bola](img/img06.jpg)

Agora podemos executar novamente nosso projeto para visualizarmos o resultado.

![jogadores e bola 2](img/img07.jpg)

## Dando Movimento a Bola de Jogo.

Antes de iniciarmos os códigos para movimentarmos a bola  no jogo vamos organizar os códigos que posicionam os elementos de jogador de da bola na janela de jogo.

Para isso crie uma função desenho() conforme o código abaixo e mova (recorte e cole) todas as linhas de "blit" (linhas 12, 15, 16 e 20 do código mostrado anteriormente) para dentro da função desenho. Faça conforme demonstrado abaixo:

![jogadores e bola 2](img/img08.jpg)

Agora vamos criar duas variáveis para controlar a posição atual da bola dentro do campo de jogo, essas variaveis de chamarão bola_x e bola_y (linhas 16 e 17 ) e 
aproveite e substitua na linha 22 do blit da bola atualize as posições 617 para bola_x e 337 para bola_y ficando conforme o código abaixo.

![jogadores e bola 2](img/img09.jpg)

Assim conseguiremos atualizar a posição da bola dinamicamente durante o jogo.

Agora vamos definir a função que nos permitirá fazer o movimento da bola. Digite o código conforme abaixo.

![jogadores e bola 2](img/img10.jpg)

As linha 27 e 28 capturam o valor das variaveis bola_x e bola_y que estão fora da função, e logo a seguir na linha atualizamos a posição X da bolinha.

Também não podemos de esquecer de atualizrmos nosso main com as funções agora criadas desenho() e movimenta_bola(), para isso atualize o seu código como abaixo.

![jogadores e bola 2](img/img11.jpg)

Execute seu código e verifique se sua bolinha ganhou movimento. Você pode obserar que sim mas temos que estabelecer limites e a interação com a movimentação dos jogadores durante a partida.


