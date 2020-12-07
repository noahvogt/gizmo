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
