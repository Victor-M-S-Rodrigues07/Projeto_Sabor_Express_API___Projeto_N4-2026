from Atividades_Curso.Atividade_N1.Banco.banco import Banco

class Agencia (Banco):

    def __init__ (self, nome, endereco, numero):

        super().__init__ (nome, endereco)
        self.numero = numero