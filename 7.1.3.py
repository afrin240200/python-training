def remove_repeated_characters(string):
    unique_chars = []
    for char in string:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)

if __name__ == "__main__":
    string = input("Enter a string: ")

    result = remove_repeated_characters(string)

    print("String after removing repeated characters:", result)

