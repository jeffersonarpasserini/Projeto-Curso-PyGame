# Aula01 - Introdução ao Python

## Python

Python é uma linguagem de programação interpretada, orientada a objetos, de alto nível e com semântica dinâmica. A simplicidade do python reduz a manutenção de um programa.
A linguagem suporta módulos e pacotes, que encoraja a modularização e o reuso de códigos.

É uma das linguagens  que mais tem crescido devido a sua compatibilidade e capacidade de auxiliar outras linguagens, é também um das  linguagens mais populares entre a comundade de análise de dados e a comunidade cientifica.

## História do Python

A linguagem Python foi criada em 1990 por Guido Van Rossum no Centro de Matemática Stichting (CWI - http://www.cwi.nl) na Holanda como sucessora da linguagem ABC. Guido é lembrado como o principal autor do Python, mas outros programadores ajudaram com muitas contribuições.

A linguagem ABC foi desenhada para o uso de não programadores, mas logo de início mostrou certas limitações e restrições, a grande reclamação era a presença de regras arbitrárias que geralmente eram utilizadas em linguagens de baixo nível.

O Python surigiu para que fosse uma linguagem simples que possuísse algumas das melhores propriedades da linguagem ABC. Listas, dicionários, declarações básicas e uso obrigatório de identação diferenciam a linguagem Python da linguagem ABC.

Em 1995, Guido continuou seu trabalho em Python na Corporation for National Research Initiatives (CNRI, http://cnri.reston.va.us). Em 2000 o time de desenvolvimento da linguagem foram para a BeOpen Python Labs (http://beopen.com), no mesmo ano mudaram-se para a Digital Creations, hoje Zope Corporation (http://www.zope.org).

Em 2001 foi fundada a Python Software Fundation (PSF - http://www.python.org/psf/), uma organização sem fins lucrativos fundada para manter a lingaugem e hoje detem sua propriedade intelectual.

Todos os lançamentos de novos releases da linguagem Python são de código aberto.

## Interpretador

Você já deve ter ouvido falar que a linguagem Python é interpretada ou uma linguagem de script. em certo sentido pode-se afirmar que é uma linguagem interpretada, mas na verdade a forma de execução de programas python atualmente assemelha-se a forma de execução da linguagem Java.

O interpretador faz a tradução em tempo real para código de máquina, ou seja, em tempo de execução. Já um compilador traduz o programa inteiro em código de máquina em uma única vez, gerando um relatório de erros caso existam ou gerando o programa que pode ser rodado (executável).

O  Python é uma linguagem interpretada mas como o Java, passa por um processo de compilação gerando um bytecode e depois é interpretado por uma máquina virtual.

## É possível compilar o Python ?

Existem implementações de compiladores para Python como o Cpython, Cython, Jython, IronPython ou PyPy. A diferença entre elas é o compilador.

o Cpython é o compilador oficial da linguagem Python quando você a utiliza por padrão. O Cython converte a linguagem Python para C++e utiliza o compilador desta linguagem para gerar o executável, mas para ser eficiente deve adaptar o código python original.

O Jython gera bytecode a partir do Python para ser executado na JVM (Java Virtual Machine) e o IronPython em uma máquina virtual .Net.

O PyPy é uma implmentação escrita em python que possui uma Virtual Machine Python sendo mais veloz que o CPython origianl e vem com a tecnologia JIT (Just in Time) que já traduz o código fonte em linguagem de máquina.

## Modo Script ou Interativo

Para utilizar o modo interativo você deve abrir o terminal do seu sistema operacional e rodar o python. Por exemplo:

**C:\python**

Você terá acesso ao prompt do Python para a digitação de suas instruções:

![Prompt Python](img/python_prompt.jpg)

No modo script você pode utilizar qualquer editor de texto para escrever o seu código python gerando um arquivo com a extensão .py. Pode utilizar qualquer IDE que desejar como o PyCharm, VSCode, Spyder entre outras existentes no mercado.

## Variáveis

Variáveis são pequenos espaços de memória, tuilizados para armazenar e manipular dados. Em Python, os tipos de dados básicos são: o tipo inteiro (armazena números inteiros), o tipo float (armazena números em formato decimal), tipo string (armazena um conjunto de caracteres) e o tipo booleano ( que armazena verdadeiro ou falso). Cada variável pode armazenar apenas 1 tipo de dado a cada instante.

Em Python diferentemente de outras lingaugeens de programação que você está acostumado a utilizar como o Java ou C/C++ não é preciso declarar de que tipo será cada variável no programa. Quando se faz uma atribuição de valor, automaticamente a variável se torna do tipo do valor armazenado, como nos exemplos a seguir:

**>> a=10 - valor inteiro**

**>> nome = "Joaquim" - string**

**>>ok=True - valor booleano**

**>>salario=10500.52 - valor decimal (float)**

Em Python os nomes das variáveis devem ser iniciados com uma letra, mas podem possuir outros tipos de caracteres, como números e símbolos. O símbolo sublinhado ( _ ) também é aceito no ínico de nomes de variáveis, exemplos de nomes válidos e invalidos:

**Válidos:**
a3, velocidade, velocidade90, salario_medio, _salario

**Invalidos**
salário_médio, salario medio, 5A,

Nossos nomes de variáveis não podem ter espaços em branco e devemos evitar o uso de acentos.

## Entrada de dados

O python possui uma função de captura para as entradas do usuário: a função input(). Quando essa função é chamada, o programa espera o usuário digitar alguma coisa. Quando o usuário aperta a tecla ENTER, o programa processa e imprime na tela o valor digitado em forma de String.

Deste modo as entradas de dados serão sempre no formato String, como no exemplo abaixo a variavel salario e a variavel nome serão do tipo String.

**salario = input("Entre com o seu salario: ")**

**nome = input("Entre com o seu nome: ")**

## Conversão de Tipos de Dados

A função  input() lê o valor digitado pelo usuário como uma string.

**salario = input("Entre com o seu salario: ")**

Se o usuário digitar o número 1400 a variável salario armazenará a string "1400", podemos checar isso com a função type():

**type(salario)**
retorno: 
**class 'str'**

Para conseguirmos receber um valor inteiro ou decimal devemos utilizar funções de conversão: **int()**, **float()** ou **complex()** se por acaso utilizarmos números complexos.
Podemos também fazer a conversão de númericos para string com a função **str()**.

**salario = float(input("Entre com o seu salario: "))**

No exemplo acima a função input() receberá um valor String que será convertido para o tipo float pela função float() e armazenado na variavel salario.

## Saída de Dados

Para a saída de dados o Python possui a função print(). Por exemplo podemos exibir o valor digitado anteriormente na variável salario da seguinte forma:

**print("O salario informado foi: " + salario)**

Neste exemplo concatenamos a string com a variável salario (de tipo string) com o operador +. Outra maneira mais elegante é usar a função format():

**print("O sálario informado foi de {} reais".format(salario))**

Se tentarmos concatenar a saida na função print() com uma variavel numérica ocasionará um erro de execução.

**print("O valor da venda foi "+valor_venda)**

![Erro: concatenação de variavel numérica na saída de dados](img/erro_concat_string.jpg)

Podemos corrigir esse problema utilizando a função **format()**. Está função faz parte de um conjunto de formatação de Strings chamada formatter, que é composto por outras funções de formatação mas a função format é a principal e mais utilizada.

Com ela podemos passar parâmetro de qualquer itpo, além de ser extremamente útil para formatar números passando o seu format code. Por exemplos, podemos arredondar um número ponto flutuante como 300.565656789 para duas casas decimais ou fazer a saída do valor da venda corretamente.

**print("O valor da venda foi {:.2f}".format(valor_venda))**

**numero_pto_flutuante = 300.565656789** 

**print("numero ponto flutuante : {:.2f}".format(numero_pto_flutuante))**

## Manipulação de Strings

Em Python existem várias funções para manipular Strings. Na tabela abaixo são apresentados os principais métodos.








## Operadores Aritméticos

![Operadores Aritméticos](img/operadores_aritmeticos.jpg)

## Operadores de Comparação

![Operadores Comparação](img/operadores_comparacao.jpg)

## Operadores Lógicos

![Operadores Lógicos](img/operadores_logicos.jpg)












