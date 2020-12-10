
# doubles duration
def vergrösserung(input_list):
    working_list = []
    for n in input_list:
        note = n
        duration = float (note[0:4]) * 2
        note = duration_to_string(duration) + note[4:]
        working_list.append(note)
    return working_list

# halfs duration
def verkleinerung(input_list):
    working_list = []
    for n in input_list:
        note = n
        duration = float(note[:4]) / 2
        note = duration_to_string(duration) + note[4:]
        working_list.append(note)
    return working_list

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

