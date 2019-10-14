# Linguagem de Programação II
# AC06 ADS2C - Faculdade
# alunos: aluno1.sobrenome@aluno.faculdadeimpacta.com.br
#         aluno2.sobrenome@aluno.faculdadeimpacta.com.br


class Disciplina:
    '''
    Abstração de uma disciplinai, possui os atributos Nome e carga Horária
    '''
    def __init__(self, nome: str, carga_horaria: int) -> None:
        self._nome = nome
        self._carga_horaria = carga_horaria

    def get_nome(self) -> str:
        '''
        Acessor do atributo nome
        '''
        return self._nome

    def get_carga_horaria(self) -> int:
        '''
        Acessor do atributo cargar horaria
        '''
        return self._carga_horaria


class Pessoa:
    '''
    Abstração de uma pessoa no Modelo, classe base para Aluno e Professor
    que contém dados pertencentes a ambos.
    '''
    def __init__(self, nome: str, telefone: int, email: float) -> None:
        self._nome = nome
        self._telefone = telefone
        self._email = email 

    def get_nome(self) -> str:
        '''
        Acessor do atributo Nome
        '''
        return self._nome

    def get_telefone(self) -> int:
        '''
        Acessor do atributo telefone
        '''
        return self._telefone

    def set_telefone(self, novo_telefone: int) -> None:
        '''
        Mutador do atributo telefone deve checar se é um número inteiro e,
        caso contrário devolver um TypeError
        '''
        if type(novo_telefone) == int:
            return TypeError

    def get_email(self) -> str:
        '''
        Acessor do atributo email
        '''
        return self._email

    def set_email(self, novo_email) -> None:
        '''
        Mutador do atributo eail, deve checar se éum email válido
        (se possuir o caractere '@') e caso contrário devolver
        um ValueError
        '''
        if '@' in novo_email:
            self._email = novo_email
        else:
            raise ValueError


class Aluno(Pessoa):

    def __init__(self, nome: str, telefone: int,
                 email: str, n_matricula: int) -> None:
        super().__init__(nome, telefone,email)
        self._n_matricula = n_matricula

    def get_matricula(self) -> int:
        '''
        Acessor do atributo matricula
        '''
        return n_matricula

    def matricular(self, disciplina: Disciplina) -> None:
        '''
        Realiza matrícula do Aluno na disciplina
        '''
        pass

    def lista_disciplinas(self) -> list:
        '''
        Devolve a lista de disciplinas em que o aluno esta matriculado
        '''
        pass


class Professor(Pessoa):
    '''
    Entidade professor do Modelo
    '''
    def __init__(self, nome, telefone, email):

        super().__init__(nome, telefone,email)

    def ministra(self, disciplina: Disciplina) -> None:
        '''
        Atribui o professor como ministrante da disiciplina
        Um professor não pode dar mais de 200 horas de aula,
        Caso um professor tente atribuir mais de 200h devolve
        ValueError
        '''
        self.disciplina = 0
        if self._carga_horaria > 200:
            raise ValueError
        else:
            return self.disciplina

    def lista_disciplinas(self) -> list:
        '''
        lista as disciplinas ministradas pelo professor
        '''
        pass
