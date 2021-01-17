def run_length_encoding(string):
    current_run_length = 1
    encoding_string_characters = []

    for i in range(1, len(string)):
        previous = string[i - 1]
        current = string[i]

        if previous != current or current_run_length == 9:
            encoding_string_characters.append(str(current_run_length))
            encoding_string_characters.append(previous)
            current_run_length = 0

        current_run_length += 1
    encoding_string_characters.append(str(current_run_length))
    encoding_string_characters.append(string[-1])
    return ''.join(encoding_string_characters)


if __name__ == '__main__':
    output = run_length_encoding("AAAAAAAAAAAAABBCCCCDD")
    print(output)
