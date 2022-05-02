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

**C:\Python**

Você terá acesso ao prompt do Python para a digitação de suas instruções:

![Prompt Python](img/python_prompt.jpg)

No modo script você pode utilizar qualquer editor de texto para escrever o seu código python gerando um arquivo com a extensão .py. Pode utilizar qualquer IDE que desejar como o PyCharm, VSCode, Spyder entre outras existentes no mercado.

## Variáveis


