# Linguagem de Programação II
# AC02 ADS2D - Conta Palavras
# alunos: gabriel.rocha@aluno.faculdadeimpacta.com.br
#         rafael.apolinario@aluno.faculdadeimpacta.com.br

from typing import Dict, Tuple
import auxiliares as aux

def conta_palavras_biblia() -> Dict[str, int]:
    '''
    Devolve um Dicionário Python onde cada chave é uma palavra da Bíblia
    e o valor associado é frequência absoluta dessa palavra na Bíblia.
    Considere como palavra uma sequência de caractéres separados por espaço,
    (utilize o método split da classe string)
    '''
    palavras_biblia = {}
    for linha in aux.le_biblia():
        for palavra in linha.split():
            if not palavra in palavras_biblia:
                palavras_biblia[palavra] = 1
            else:
                palavras_biblia[palavra] += 1
    return palavras_biblia

def palavra_mais_frequente(frequencias: Dict[str, int]) -> Tuple[str, int]:
    '''
    Função que recebe um dicionário com freqûencias e encontra a chave com
    o maior valor associado
    '''
    maior = 0
    valor = 0
    for maiores, valores in frequencias.items():
        if valores > valor:
            maior = maiores
            valor = valores    
    tpl = (maior, valor)    
    return tpl
    
def mais_frequente_biblia() -> Tuple[str, int]:
    '''
    Função que retorna a palavra mais frequênte presente na Bíblia.
    '''
    maior = 0
    valor = 0
    x = conta_palavras_biblia()
    for maiores, valores in x.items():
        if valores > valor:
            maior = maiores
            valor = valores        
    tupla = (maior, valor)
    return tupla

print(mais_frequente_biblia(palavra))