def sort_string(string):
    chars = list(string)
    chars.sort()
    sorted_string = ''.join(chars)

    return sorted_string

if __name__ == "__main__":
    input_string = input("Enter the input string: ")

    output_string = sort_string(input_string)

    print("The output string:", output_string)

