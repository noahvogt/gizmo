# plays inputed higher by a value. By now only works upwards (positiv values) and can 
# cause weird notation like G#- with F- and 2 
def sequenz(input_list, value):
    notes_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    working_list = []
    for n in input_list:
        note = n[:4]
        pitch = n[4:5]
        ord_number = notes_list.index(pitch)
        octave = int(n[-1:])
        ord_number += value
        while ord_number >= 12:
            octave += 1
            ord_number = ord_number - 12
        if n[5:6] == '#':
            note = note + notes_list[ord_number] + '#' + str(octave)
            working_list.append(note)
        elif n[5:6] == '-':
            note = note + notes_list[ord_number] + '-' + str(octave)
            working_list.append(note)
        else:
            note = note + notes_list[ord_number] + str(octave)
            working_list.append(note)
    return working_list

# work in progress ...
def convert_multiple_key_signetures(note):
    notes_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    while len(note) > 7:
        if note[5:7] == "##":
            note[4:5]
        if note[5:7] == "--":
        if note[5:7] == "-#" or note[4:6] == "#-":
            note = note[:5] + note[7:]
    return note
l = ['1.00D#5', '0.25F-4', '0.50C5']
print (l)
print(sequenz(l, 3))