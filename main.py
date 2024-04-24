notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        # 0    1     2    3     4    5    6     7    8     9    10   11

escala_maior = [2,2,1,2,2,2]
escala_menor = [2,1,2,2,1,2]

while True:
    tom = input('Acorde: ').upper()
    pos = notes.index(tom)

    nota_natural = [tom]
    for i in escala_maior:
        pos += i
        if pos >= len(notes):
            pos -= len(notes)

        if i == 1:
            nota_atual = notes[pos]
            nota_anterior = notes[pos - i]

            if nota_anterior in nota_atual:
                nota_natural.append(notes[pos] + "/" + notes[pos + 1] + "b")
            else:
                nota_natural.append(notes[pos])
        else:
            nota_natural.append(notes[pos])
    print(nota_natural)