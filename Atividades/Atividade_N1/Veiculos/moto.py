from Atividades.Atividade_N1.Veiculos.veiculo import Veiculo

class Moto (Veiculo):

    def __init__ (self, marca, modelo, tipo):

        super().__init__ (marca, modelo)
        self.tipo = tipo

    def __str__ (self):

        return f"{super(),__str__()} | Tipo: {self.tipo}"