def string_length(string):
    return len(string)

def string_copy(string):
    return string[:]

def string_concatenate(string1, string2):
    return string1 + string2

def string_to_uppercase(string):
    return string.upper()

def compare_strings(string1, string2):
    if string1 < string2:
        return "First string is alphabetically before second string."
    elif string1 > string2:
        return "First string is alphabetically after second string."
    else:
        return "Both strings are equal."

if __name__ == "__main__":
    first_string = input("Enter the first string: ")
    second_string = input("Enter the second string: ")

    print("Length of first string:", string_length(first_string))
    print("Length of second string:", string_length(second_string))

    print("Copy of first string:", string_copy(first_string))

    concatenation = string_concatenate(first_string, second_string)
    print("Concatenation of both strings:", concatenation)

    uppercase_first = string_to_uppercase(first_string)
    print("Uppercase of first string:", uppercase_first)

    comparison_result = compare_strings(first_string, second_string)
    print(comparison_result)

