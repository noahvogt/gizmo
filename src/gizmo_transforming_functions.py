
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
    conv_note = note
    note = note.split(',')
    while len(note[1]) > 3:
        if note[1][1:3] == "##":
            note[1] = note[1][:1] + note[1][-1:] #remove ##
            conv_note = note[0] + ',' + note[1] #built new note
            conv_note = highes_note(conv_note, 2) #highes note by 2
        elif note[1][1:3] ==  "--":
            note[1] = note[1][:1] + note[1][-1:] #remove --
            conv_note = note[0] + ',' + note[1] #built new note
            conv_note = highes_note(conv_note, -2) #highes note by 2
        elif note[1][1:3] == "-#" or note[1][1:3] == "#-":
            note[1] = note[1][:1] + note[1][-1:] #remove #- or -#
            conv_note = note[0] + ',' + note[1] #built new note
    return conv_note

# returns the pitch difference from two notes
# assumes that last char is octave indicater
def interval(note_1, note_2):
    notes_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    note_1 = note_1.split(',')
    note_2 = note_2.split(',')
    octave = int(note_2[1][-1:]) - int(note_1[1][-1:])
    pitch = notes_list.index(note_2[1][:1]) - notes_list.index(note_1[1][:1])
    pitch += 12 * octave
    if note_1[1][1:2] == '#': pitch -= 1
    if note_2[1][1:2] == '-': pitch -= 1
    if note_1[1][1:2] == '-': pitch += 1
    if note_2[1][1:2] == '#': pitch += 1
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
    note = note.split(',')
    notes_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    is_up = True
    if value < 0: # check if value is negative and store in is_up
        notes_list.reverse()
        value = -value
        is_up = False
    pitch = note[1][:1] # first char from 2nd list argument
    ord_number = notes_list.index(pitch)
    octave = int(note[1][-1:])
    ord_number += value
    while ord_number >= 12:
        if is_up:
            octave += 1
        else:
            octave -= 1
        ord_number = ord_number - 12
    if note[1][1:2] == '#': # 2nd char from 2nd list argument
        higher_note = note[0] + ',' + notes_list[ord_number] + '#' + str(octave)
    elif note[1][1:2] == '-':
        higher_note = note[0] + ',' + notes_list[ord_number] + '-' + str(octave)
    else:
        higher_note = note[0] + ',' + notes_list[ord_number] + str(octave)
    higher_note = convert_multiple_key_signetures(higher_note)
    return higher_note

# returns a part higher by some value
def sequenz(input_list, value):
    working_list = []
    for n in input_list:
        note = highes_note(n, value)
        working_list.append(note)
    return working_list

# mirrors notes at the first note
def mirror_pitch(input_list):
    working_list = []
    mirror = input_list[0]
    for note in input_list:
        pitch = highes_note(mirror, - interval(mirror, note)) # change pitch
        note = note.split(',')
        pitch = pitch.split(',')
        mir_note = note[0] + ',' + pitch[1] # take duration from "note"
        working_list.append(mir_note)
    return working_list

# mirrors the rythme from back to front
def mirror_rythm(input_list):
    r_input_list = input_list[::-1]
    working_list = [] # revesed list
    for i in range (0, len(input_list)):
        r_note = r_input_list[i].split(',')
        n_note = input_list[i].split(',')
        working_list.append(r_note[0] + ',' + n_note[1]) 
    return working_list


# reverses list of notes (krebs)
def krebs(input_list):
    return input_list[::-1]
