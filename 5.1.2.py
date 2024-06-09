def search_element(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1
arr = [5, 10, 15, 20, 25]
element = int(input("Enter the element you want to search for: "))

position = search_element(arr, element)
if position != -1:
    print(f"The element {element} is found at position {position}.")
else:
    print("The element is not found in the array.")

