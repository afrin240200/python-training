def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":
    n = int(input("Enter how many values you want to read: "))
    array = []
    for i in range(n):
        value = int(input(f"Enter the value of a[{i}]: "))
        array.append(value)

    bubble_sort(array)

    print("Array sorted in ascending order =", end=" ")
    for num in array:
        print(num, end=" ")
    print()

