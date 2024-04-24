from escalas import escala_default
from tonalidade import return_tonality


def gerar_escala(tonica: str, tonalidade: str):
    """
    Apartir de uma tônica e uma tonalidade, é gerado uma escala

    Argument:
        :param tonica: nota fundamental ou base, para determinar a escala
        :param tonalidade: indicamos o tipo de escala (maior ou menor)

    Return:
        :param base: um dicionário com a escala modificada
    """
    base = []
    pos_tonica = 0
    try:
        tonica = tonica.upper()
        tonalidade = return_tonality(tonalidade)  # func return_tonality: retorna um dicionário com os intervalos (
        # Maiores ou menores) e a posição do primeiro semi-ton, usado para informar a enarmonia
        # Tonalidade - [[intervalos - dict],[enarmonia - int]]
        pos_tonica = escala_default.index(tonica)  # dict escala_default = dicionario com todas as notas
    except ValueError as error:
        print(error)
        return
    for pos in tonalidade[0]:  # Monta a escala maior/menor com base aos dados fornecidos.
        nota = (pos_tonica + pos) % 12
        if pos == tonalidade[1][0] and escala_default[nota - 1] in escala_default[nota]:
            # Primeiro bloco valida a posição na escala
            # Segundo bloco valida, se a nota anterior e parecida a enarmonia.
            # ex: [A] == [A#] => true
            base.append(escala_default[nota] + "/" + escala_default[nota + 1] + "b")
        else:
            base.append(escala_default[nota])
    return base
