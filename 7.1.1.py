def count_character_frequency(string):
    frequency = {}

    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency

if __name__ == "__main__":
    string = input("Enter a string: ")

    frequency = count_character_frequency(string)

    print("Character frequencies:")
    for char, freq in frequency.items():
        print(f"'{char}': {freq}")

