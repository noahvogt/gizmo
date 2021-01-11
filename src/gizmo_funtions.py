# function to return only a selected 'part' from each line of the 'gizmo notation'
def return_part(input_list, split_index):
    # create a temporary list with the selected 'part'
    working_list = []
    for sub in input_list:
        working_list.append((sub.split(",")[split_index]))

    return working_list

# function to replace a substring of a 'part' from each line of the 'gizmo notation'
def replace_substring_of_list_part(input_list, split_index, pattern, replace_str):

    # create a temporary list with the selected 'part'
    working_list = []
    for sub in input_list:
        working_list.append((sub.split(",")[split_index]))

    # replace the patterns in the temporary list with the replacement strings
    working_list = [sub.replace(pattern, replace_str) for sub in working_list]

    # replace the new 'part' segment in each line 
    output_list = []
    seperator_string = ","
    for i in range(len(input_list)):
        loop_list = input_list[i].split(",")
        loop_list[split_index] = working_list[i]
        output_list.append(seperator_string.join(loop_list))
    input_list[:] = output_list

# return true if the given pitch is in correct gizmo notation
notes_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def check_pitch_gizmo_notation(pitch):
    if pitch[0] not in notes_list:
        return False
    if len(pitch) == 2:
        if pitch[1].isdigit():
            return True
        else:
            return False
    elif len(pitch) == 3:
        if pitch[1] == '-' or pitch[1] == '#' and pitch[2].isdigit():
            return True
    else:
        return False

# function to write to standard output in the 'gizmo notation'
def gizmo_stdout(input_list):
    for item in input_list:
        print(item)

# function to write to a (new) file in the 'gizmo notation'
def gizmo_write2file(input_list, path_to_file):
    with open(path_to_file, "w+") as file_writer:
        for item in input_list:
            file_writer.write(item+"\n")
        file_writer.close()

# function to read from standard input and return it a list of each line
def stdin():
    stdin_list = []
    import sys
    for line in sys.stdin:
        stdin_list.append(line.rstrip())
    return stdin_list

# this funcion takes a text and return every char that occuers once in a list
def diff_char(text):
    char_list = []
    for char in text:
        if char in char_list:
            continue
        else:
            char_list.append(char)
    return char_list

# This function checks if the given tempi is in correct notation and
# returns a boolean value
def check_tempo_gizmo_notation(tempo):
    if len(tempo) != 4:
        return False
    elif tempo[1:2] != '.':
        return False
    else:
        tempo = tempo[:1] + tempo[2:]
        if not tempo.isdigit():
            return False
        else:
             return True

# this function deletes whitespaces from gizmo notation and return a boolean value if 
# it is okay or not.
def check_gizmo_notation(name):
    with open(name, "r") as file_opener:
        content = file_opener.read()
    content = content.replace(" ", "")
    content = content.strip()
    content_list = content.split('\n')
    # remove all empty notes
    working_list = content_list[:]
    for i in content_list:
        if i == '':
            working_list.remove('')
    content_list = working_list
    gizmo_write2file(content_list, name)
    try:
        for line in content_list:
            parts = line.split(',')
            if not check_pitch_gizmo_notation(parts[1]):
                return False
            if not check_tempo_gizmo_notation(parts[0]):
                return False
        return True
    except(IndexError):
        return False
