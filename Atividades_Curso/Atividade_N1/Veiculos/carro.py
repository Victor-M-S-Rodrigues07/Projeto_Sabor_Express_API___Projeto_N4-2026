from Atividades_Curso.Atividade_N1.Veiculos.veiculo import Veiculo


class Carro (Veiculo):

    def __init__ (self, marca, modelo, quantidade_portas):

        super().__init__ (marca, modelo)
        self.quantidade_portas = quantidade_portas

    def __str__ (self):

        return f"{super().__str__()} \nTipo da moto: {self.tipo}"