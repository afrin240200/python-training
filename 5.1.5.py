import math
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)
def calculate_variance(numbers, mean):
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)
def calculate_deviation(variance):
    return math.sqrt(variance)
if __name__ == "__main__":
    numbers = []
    n = int(input("Enter the number of elements: "))
    print("Enter the numbers:")
    for i in range(n):
        numbers.append(float(input()))
        mean = calculate_mean(numbers)
        variance = calculate_variance(numbers, mean)
        deviation = calculate_deviation(variance)
    print(f"Mean: {mean}")
    print(f"Variance: {variance}")
    print(f"Deviation: {deviation}")

