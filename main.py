notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        # 0    1     2    3     4    5    6     7    8     9    10   11

n = {'C': 0, 'C#': 0.5, "D": 1, "D#": 1.5, "E": 2, "F": 2.5, "F#": 3, "G": 3.5, "G#": 4, "A": 4.5, "A#": 5, "B": 5.5}


escala_maior = [2,2,1,2,2,2,1]
tom = 'C'
pos = notes.index(tom)

indice = n[n]

for intervalo in escala_maior:
    # Incrementar o índice pela quantidade de semitons do intervalo
    indice += intervalo
    # Se o índice ultrapassar 11 (o número total de notas cromáticas), voltamos ao início da lista
    indice = indice % 12
    # Adicionar a próxima nota da escala à lista
    for key, value in n.items():
        if value == indice:
            escala.append(key)
            break

'''while True:

    tom = input('Acorde: ').upper()
    pos = notes.index(tom)

    nota_natural = [tom]
    for i in escala_maior:
        pos += i
        if pos >= len(notes):
            pos -= len(notes)

        nota_natural.append(notes[pos])


        ultima_nota = [nota_natural[-2], nota_natural[-1]]

        if ultima_nota[0] in ultima_nota[1]:
            nota_natural[-1] = notes[pos + 1] + "b"


    print(nota_natural)'''