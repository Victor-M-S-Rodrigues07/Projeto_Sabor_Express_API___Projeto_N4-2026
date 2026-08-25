from Atividades_Curso.Atividade_N1.Veiculos.veiculo import Veiculo

class Moto (Veiculo):

    def __init__ (self, marca, modelo, tipo):

        super().__init__ (marca, modelo)
        self.tipo = tipo