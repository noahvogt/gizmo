
""" helper functions """

# converts float duration to string in the form x.xx
def duration_to_string(input_float_duration):
    input_float_duration *= 100
    input_int_duration = int(input_float_duration)
    duration = ""
    for i in range (0, 3):
        x = input_int_duration % 10
        duration = duration + str(x)
        input_int_duration = input_int_duration // 10
    duration = duration[::-1]
    duration = duration[:1] + '.' + duration[1:]
    return duration

# converts the weird notation like -#, ## or -- to nothing, one note higher or lower respectivly
def convert_multiple_key_signetures(note):
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

def interval(note_1, note_2):
    notes_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octave = int(note_2[-1:]) - int(note_1[-1:])
    pitch = notes_list.index(note_2[4:5]) - notes_list.index(note_1[4:5])
    pitch += 12 * octave
    if note_1[5:6] == '#': pitch -= 1
    if note_2[5:6] == '-': pitch -= 1
    if note_1[5:6] == '-': pitch += 1
    if note_2[5:6] == '#': pitch += 1
    return pitch
    
""" actual functions """

# changes tempo
def tempo(input_list, temp):
    working_list = []
    for note in input_list:
        duration = float (note[0:4]) * temp
        note = duration_to_string(duration) + note[4:]
        working_list.append(note)
    return working_list

# half duration
def verkleinerung(input_list):
    return tempo(input_list, .5)

# double duration
def vergrösserung(input_list):
    return tempo(input_list, 2)

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
    while ord_number >= 12:
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

# returns a part higher by some value
def sequenz(input_list, value):
    working_list = []
    for n in input_list:
        note = highes_note(n, value)
        working_list.append(note)
    return working_list

# mirrors notes at the first note
def mirror(input_list):
    working_list = []
    mirror = input_list[0]
    for note in input_list:
        tmp_note = highes_note(mirror, - interval(mirror, note))
        print (tmp_note)
        working_list.append(tmp_note)
    return working_list