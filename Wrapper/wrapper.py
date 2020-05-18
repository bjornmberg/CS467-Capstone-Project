def wrap_processor(string):
    """Processes input string and outputs wrapped as TextWrapper does, without stripping special chars

    :param string: String for wrapping
    :return: Array containing wrapped strings
    """
    # Establish variables for use in processing
    wrapped = ''
    list_for_processing = []
    counter = 0
    width = 80

    mid_processing_list = []

    # If newline, split lines and process
    if '\n' in string:
        splitLinesList = string.splitlines()

        # For each line in array. The following is adapted from a post on
        # https://stackoverflow.com/questions/16430200/a-good-way-to-make-long-strings-wrap-to-newline
        for x in splitLinesList:
            # Split each by word and process
            list_for_processing = x.split()
            wrapped = '                    '
            counter = 0
            for word in range(0, len(list_for_processing)):
                # If the current word is of length that can be added to the current line, within width limit
                if counter + len(list_for_processing[word]) + 1 <= width:
                    # Add the word to the wrapped string
                    wrapped = wrapped + list_for_processing[word] + ' '
                    # Increment the counter
                    counter = counter + len(list_for_processing[word]) + 1
                else:
                    wrapped = wrapped + '\n' + '                    ' + list_for_processing[word] + ' '
                    counter = len(list_for_processing[word])
            mid_processing_list.append(wrapped)

    # Else, process a string without newlines
    # The following is adapted from a post on:
    # https://stackoverflow.com/questions/16430200/a-good-way-to-make-long-strings-wrap-to-newline
    else:
        list_for_processing = string.split()
        wrapped = '                    '
        counter = 0
        for word in range(0, len(list_for_processing)):
            # If the current word is of length that can be added to the current line, within width limit
            if counter + len(list_for_processing[word]) + 1 <= width:
                # Add the word to the wrapped string
                wrapped = wrapped + list_for_processing[word] + ' '
                # Increment the counter
                counter = counter + len(list_for_processing[word]) + 1
            else:
                # Add a newline, and the word in question. Increment counter
                wrapped = wrapped + '\n' + '                    ' + list_for_processing[word] + ' '
                counter = len(list_for_processing[word])
        # Add the string to the list for later processing
        mid_processing_list.append(wrapped)

    # Perform character substitution, replacing special marker characters with terminal commands
    final_list = []
    final_string = ''
    for x in mid_processing_list:
        for z in x:
            if z == '@':
                # Bold Red Text for Items
                new_char = '\033[1;31m'
            elif z == '^':
                # Bold Purple Text for Features
                new_char = '\033[1;35m'
            elif z == '$':
                # Bold Cyan Text for Directions
                new_char = '\033[1;36m'
            elif z == '~':
                # Bold Yellow Text for End Game Hints
                new_char = '\033[1;33m'
            elif z == '#':
                # End terminal command, reset to normal
                new_char = '\033[0m'
            else:
                new_char = z
            final_string = final_string + new_char
        final_list.append(final_string)
        final_string = ''

    return final_list