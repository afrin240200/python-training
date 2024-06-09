def display_array(arr):
    print("Array elements:", arr)
def insert_delete(arr, insert_num, insert_index, delete_index):
    if insert_index < 0 or insert_index > len(arr) or delete_index < 0 or delete_index >= len(arr):
       return "Invalid index"
    arr.insert(insert_index, insert_num)
    del arr[delete_index]
    return arr
if __name__ == "__main__":
    array = []
    n = int(input("Enter the number of elements in the array: "))
    print("Enter the elements of the array:")
    for i in range(n):
        array.append(int(input()))

    print("Array before insert and delete operations:")
    display_array(array)

    insert_num = int(input("Enter the number to insert: "))
    insert_index = int(input("Enter the index to insert: "))
    delete_index = int(input("Enter the index to delete: "))

    result = insert_delete(array, insert_num, insert_index, delete_index)
    print("Array after insert and delete operations:")
    display_array(result)

