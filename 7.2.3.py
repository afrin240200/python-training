def strcpy(source, destination, index=0):
    if index == len(source):
        return

    destination[index] = source[index]
    strcpy(source, destination, index + 1)

if __name__ == "__main__":
    first_string = input("Enter first string: ")
    second_string = input("Enter second string: ")
    destination = list(second_string)
    strcpy(first_string, destination)

    print("After copying the First string:", ''.join(destination))
    print("Second string:", ''.join(destination))

