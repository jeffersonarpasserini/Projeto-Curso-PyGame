#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:45:54 2022

@author: jeffersonpasserini
"""

#criacao de variáveis
idade=15
valor_troco=10.55
verdadeiro=True
false=False


#exemplos de entrada de dados
salario = input("Entre com o seu salario: ")
print(type(salario))


nome = input("Informe o seu nome: ")
print(type(nome))

#conversão de dados
valor_venda = float(input("Informe o valor da venda: "))
print(type(valor_venda))

#saida de dados
print("O salario informado foi: " + salario)

print("O sálario informado foi de {} reais".format(salario))


#print("O valor da venda foi "+valor_venda) #gera erro de execução

#saida valor da venda
print("O valor da venda foi {:.2f}".format(valor_venda))
#arredondamento ponto flutuante
numero_pto_flutuante = 300.565656789
print("numero ponto flutuante : {:.2f}".format(numero_pto_flutuante))


