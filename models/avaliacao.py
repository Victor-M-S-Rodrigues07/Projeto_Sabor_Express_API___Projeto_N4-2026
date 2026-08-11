class Avaliacao:

    """ Representa uma avaliação de um restaurante. """

    def __init__ (self, cliente, nota):

        """ Inicializa uma avaliação com o nome do cliente e a nota atribuída. """

        self._cliente = cliente

        if nota > 5 or nota < 0:

            self._nota = None

        else:

            self._nota = nota