from models.avaliacao import Avaliacao

class Restaurante:

    """ Representa um restaurante e suas características. """

    restaurantes = []   # Atributo da classe

    def __init__ (self, nome, categoria):

        """ 
        Inicializa um restaurante com nome, categoria, status e avaliações. 
        
        Parâmetros:
        
        - nome (str): Nome do restaurante.
        - categoria (str): Categoria do restaurante.
        """

        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []        # Lista porque vários clientes adicionam avaliações. Só se manipula depois, não na instanciação
        Restaurante.restaurantes.append (self)

    def __str__(self):

        """ Representa o restaurante como uma String"""

        return f"{self._nome} | {self._categoria}"
    

    @classmethod

    def listar_restaurantes (cls):

        """ Lista todos os restaurantes cadastrados. """

        print(f"{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}")

        for restaurante in cls.restaurantes:        # A classe tem o atributo lista de restaurantes

            print (f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")   # Não se puxa o self pois estamos pegando da lista

    @property

    def ativo (self):

        """ Cria uma propriedade para a representação do status do restaurante. """

        return "■" if self._ativo else "□"
    

    def alternar_estado (self):

        """ Alterna o status do restaurante entre ativo e inativo. """

        self._ativo = not self._ativo       # Not: inverte a lógica booleana

    def receber_avaliacao (self, cliente, nota):

        """
        Recebe a avaliação de um cliente e a adiciona à lista de avaliações do restaurante.
        
        Parâmetros:
        - cliente (str): Nome do cliente.
        - nota (float): Nota atribuída ao restaurante (de 0 a 5).
        """

        avaliacao = Avaliacao (cliente, nota)
        self._avaliacao.append (avaliacao) if avaliacao._nota is not None else print ("Nota inválida. Serão aceitos somente números de 0 a 5. Avaliação não registrada.")


    @property       
    
    # Ser capaz de ler para cada restaurante, É um atributo do restaurante, não uma ação, por isso o @property. Como é necessário ler a média, não pode ser uma função comum, pois ela não é chamada, é lida. Por isso o @property. Se fosse uma ação, seria uma função comum.

    def media_avaliacoes (self):

        """ Calcula e retorna a média das avaliações do restaurante. """

        if not self._avaliacao:

            return "Ainda não há avaliações"
        
        soma_das_notas = sum (avaliacao._nota for avaliacao in self._avaliacao) # Ternário de percursão da lista
        quantidade_de_notas = len (self._avaliacao)
        media = round (soma_das_notas / quantidade_de_notas, 1)

        return media