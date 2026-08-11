from models.restaurante import Restaurante
from models.cardápio.bebida import Bebida
from models.cardápio.prato import Prato

restaurante_praca = Restaurante ("Praça", "Gourmet")
restaurante_mexicano = Restaurante ("Mexican Food", "Mexicana")
restaurante_japones = Restaurante ("Japa", "Japonesa")
restaurante_portugues = Restaurante ("Portuguesa", "Portuguesa")
restaurante_italiano = Restaurante ("Italiana", "Italiana")
restaurante_brasileiro = Restaurante ("Brasileira", "Brasileira")
restaurante_americano = Restaurante ("Americana", "Americana")
restaurante_chines = Restaurante ("Chinesa", "Chinesa")
restaurante_indiano = Restaurante ("Indiana", "Indiana")
restaurante_frances = Restaurante ("Francesa", "Francesa")

bebida_suco = Bebida ("Suco de Melancia", 5.0, "Grande")
prato_paozinho = Prato ("Paozinho", 2.00, "O melhor pão da cidade")



# restaurante_praca.receber_avaliacao ("Gui", 1)
# restaurante_praca.receber_avaliacao ("Lais", 5)
# restaurante_praca.receber_avaliacao ("Emy", 2)

# restaurante_mexicano.alternar_estado()
# restaurante_mexicano.receber_avaliacao ("Gui", 5)
# restaurante_portugues.receber_avaliacao ("Gui", 5)
# restaurante_italiano.receber_avaliacao ("Gui", 2)
# restaurante_brasileiro.receber_avaliacao ("Gui", 4.6)
# restaurante_americano.receber_avaliacao ("Gui", 3)
# restaurante_chines.receber_avaliacao ("Gui", 4)
# restaurante_indiano.receber_avaliacao ("Gui", 2.56)
# restaurante_frances.receber_avaliacao ("Gui", 2.3)

# restaurante_americano.alternar_estado()
# restaurante_brasileiro.alternar_estado()


def main ():

    print (bebida_suco)
    print (prato_paozinho)
    
if __name__ == "__main__":

    main()