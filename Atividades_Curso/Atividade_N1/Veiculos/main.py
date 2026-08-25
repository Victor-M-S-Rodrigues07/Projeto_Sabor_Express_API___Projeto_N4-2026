from Atividades_Curso.Atividade_N1.Veiculos.carro import Carro
from Atividades_Curso.Atividade_N1.Veiculos.moto import Moto

def main():

    c1 = Carro ("Toyota", "Corolla", 4)
    c2 = Carro ("Chevrolet", "Onix", 4)
    c3 = Carro ("Fiat", "Argo", 4)

    m1 = Moto ("Honda", "CG 160", "Casual")
    m2 = Moto ("Yamaha", "Factor 150", "Esportiva")
    m3 = Moto ("Honda", "CB 500F", "Casual")

    print (c1)
    print (c2)
    print (c3)
    print (m1)
    print (m2)
    print (m3)


if __name__ == "__main__":
    main()