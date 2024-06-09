def replace_first_occurrence(string, old_char, new_char):
    new_string = ""
    replaced = False

    for char in string:
        if char == old_char and not replaced:
            new_string += new_char
            replaced = True
        else:
            new_string += char

    return new_string

if __name__ == "__main__":
    string = input("Enter the string: ")
    old_char = input("Enter the character to be replaced: ")
    new_char = input("Enter the character to replace with: ")

    new_string = replace_first_occurrence(string, old_char, new_char)

    print("Resultant string:", new_string)

