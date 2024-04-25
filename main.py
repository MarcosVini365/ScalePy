import ScalePy.core.gerador_escalas as gs

if __name__ == '__main__':
    while True:
        tonica = str(input("Tônica: "))
        tonalidade = str(input('Tonalidade: '))

        gs.gerar_escala(tonica, tonalidade)