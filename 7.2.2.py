def compress_string(string):
    compressed = []
    count = 1
    compressed.append(string[0])
        if string[i] == string[i - 1]:
            count += 1
        else:
            compressed.append(str(count))
            compressed.append(string[i])
            count = 1
    compressed.append(str(count))
    return ''.join(compressed)

if __name__ == "__main__":
    string = input("Enter a string: ")
    compressed_string = compress_string(string)
    print("Compressed string:", compressed_string)

