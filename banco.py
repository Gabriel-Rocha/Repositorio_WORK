# Linguagem de Programação II
# AC05 ADS2D - Banco
#
# Alunos: aluno1.sobrenome@aluno.faculdadeimpacta.com.br
#         aluno2.sobrenome@aluno.faculdadeimpacta.com.br

from typing import Union, List, Dict

Number = Union[int, float]


class Cliente():
    """
    Classe Cliente do Banco.

    possui os atributos: nome, telefone e email, todos privados
    caso o email não seja um email válido gera um ValueError,
    caso o telefone não seja um número gera um TypeError
    """

    def __init__(self, nome: str, telefone: int, email: str):
        self._nome = nome
        self._telefone = telefone
        self._email = email

    def get_nome(self) -> str:
        """Acessor do atributo Nome."""
        self.get_nome

    def get_telefone(self) -> int:
        """Acessor do atributo Telefone."""
        self.get_telefone

    def set_telefone(self, novo_telefone: int) -> None:
        """
        Mutador do atributo telefone, caso não receba um número,
        gera um TypeError
        """
        if self.get_telefone != novo_telefone

    def get_email(self) -> str:
        """Acessor do atributo Email."""
        pass

    def set_email(self, novo_email: str) -> None:
        """
        Mutador do atributo Email, caso não receba um email válido
        gera um ValueError.
        """
        pass


class Banco():
    """
    A classe Banco deverá receber um nome em sua construção e deverá
    implementar os métodos:
    * abre_contas: abre uma nova conta, atribuindo o numero da conta em ordem
    crescente.
    * lista_contas(): apresenta um resumo de todas as contas do banco
    DICA: mantenha uma variável interna que armazene todas as contas do banco
    DICA2: utilze a variável acima para gerar automaticamente o número das
    contas do banco
    """
    def __init__(self, nome: str):
        self._nome = nome

    def get_nome(self) -> str:
        """Acessor do Atributo Nome."""
        return self._nome

    def abre_conta(self, clientes: List[Cliente], saldo_ini: Number) -> None:
        """
        Método para abertura de nova conta, recebe os clientes
        e o saldo inicial.
        Caso o saldo inicial seja menor que 0 devolve um ValueError
        """
        self.cont_conta = 0 
        saldo_ini = 0 
        contas = []
        try:
            if saldo_ini >= 0:
                    contas.append(Cliente.get_nome)
                    self.cont_conta += 1
                    contas.append(self.cont_conta)
            except ValueError:
                if saldo_ini <0:
                        return ValueError

    def lista_contas(self) -> List['Conta']:
        """Retorna a lista com todas as contas do banco."""
        contas = []
        while self.conta > 0:
            self.cont_conta.append(contas)
        return contas



class Conta():
    """
    Classe Conta.
    * Todas as operações (saque e deposito, e saldo inicial) devem aparecer
    no extrato como tuplas, exemplo ('saque', 100), ('deposito'), 200) etc.
    * Caso o saldo inicial seja menor que zero deve lançar um ValueError
    * A criação da conta deve aparecer no extrato com o valor
    do saldo_inicial, exemplo: ('saldo_inicial', 1000)
    DICA: Crie uma variável interna privada para guardar as
    operaões feitas na conta
    """

    def __init__(self, clientes: List[Cliente], numero_conta: int,
                 saldo_inicial: Number):
        pass

    def get_clientes(self) -> List[Cliente]:
        '''
        Acessor para o atributo Clientes
        '''
        pass

    def get_saldo(self) -> Number:
        '''
        Acessor para o Atributo Saldo
        '''
        pass

    def get_numero(self) -> int:
        '''
        Acessor para o atributo Numero
        '''
        pass

    def saque(self, valor: Number) -> None:
        '''
        Método de saque da classe Conta, operação deve aparecer no extrato
        Caso o valor do saque seja maior que o saldo da conta,
        deve retornar um ValueError, e não efetuar o saque
        '''
        pass

    def deposito(self, valor: Number):
        '''
        Método depósito da classe Conta, operação deve aparecer no extrato
        '''
        pass

    def extrato(self) -> List[Dict[str, Number]]:
        '''
        Retorna uma lista com as operações (Tuplas) executadas na Conta
        '''
        pass
