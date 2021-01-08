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
