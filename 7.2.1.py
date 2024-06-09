def compare_strings(str1, str2):
    if str1 == str2:
        return f"{str1} is equal to {str2}"
    elif str1 < str2:
        return f"{str1} is less than {str2}"
    else:
        return f"{str1} is greater than {str2}"

if __name__ == "__main__":
    first_string = input("Enter first string: ")
    second_string = input("Enter second string: ")

    if len(first_string) == len(second_string):
        print(f"{first_string} length is equal to {second_string} length")
    else:
        print(f"{first_string} length is not equal to {second_string} length")

    print(compare_strings(first_string, second_string))

