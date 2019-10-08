def le_biblia():
    """
    Devolve um arquivo interável com as linhas da bíblia.
    """
    return open('HolyBible.txt', 'r')


def le_teste():
    """
    Devolve um arquivo interável com as linhas do arquivo
    'ArquivoTeste.txt'.
    """
    return open('ArquivoTeste.txt', 'r')


def imprime_ordenado(dicionario):
    """
    imprime o dicionário ordenado pelas chaves
    """
    for chave in sorted(dicionario):
        print(chave, dicionario[chave])
