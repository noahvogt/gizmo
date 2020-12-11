# plays inputed higher by a value. By now can 
# cause weird notation like G#- with F- and 2

"""
def sequenz_old(input_list, value):
    notes_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    if value < 0:
        notes_list.reverse()
        value = -value
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
"""

def sequenz(input_list, value):
    working_list = []
    for n in input_list:
        note = highes_note(n, value)
        working_list.append(note)
    return working_list

# return the note higher by a value (1 = half a step)
def highes_note(note, value):
    notes_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    is_up = True
    if value < 0:
        notes_list.reverse()
        value = -value
        is_up = False
    tmp_note = note[:4]
    pitch = note[4:5]
    ord_number = notes_list.index(pitch)
    octave = int(note[-1:])
    ord_number += value
    while ord_number >= 12: #bug to fix (octave down)
        if is_up:
            octave += 1
        else:
            octave -= 1
        ord_number = ord_number - 12
    if note[5:6] == '#':
        note = tmp_note + notes_list[ord_number] + '#' + str(octave)
    elif note[5:6] == '-':
        note = tmp_note + notes_list[ord_number] + '-' + str(octave)
    else:
        note = tmp_note + notes_list[ord_number] + str(octave)
    note = convert_multiple_key_signetures(note)
    return note

# converts the weird notation like -# to something more common
def convert_multiple_key_signetures(note):
    notes_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    while len(note) > 7:
        if note[5:7] == "##":
            note = note[:5] + note[7:]
            note = highes_note(note, 2)
        if note[5:7] == "--":
            note = note[:5] + note[7:]
            note = highes_note(note, -2)
        if note[5:7] == "-#" or note[5:7] == "#-":
            note = note[:5] + note[7:]
    return note 

l = ['1.00D#5', '0.25F-4', '0.50C5']
print (l)
print(sequenz(l, 3))
print(sequenz(l, -3))

"""
print(highes_note('1.00D5', 2))
print(highes_note('1.00D5', -2))
print(highes_note('1.00D5', 13))
print(highes_note('1.00D5', -13))


print(convert_multiple_key_signetures('1.00D##5'))
print(convert_multiple_key_signetures('1.00D#-5'))
print(convert_multiple_key_signetures('1.00D--5'))
print(convert_multiple_key_signetures('1.00D5'))
"""