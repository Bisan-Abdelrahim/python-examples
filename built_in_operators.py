def built_in_operators(numbers, coordinates, student):
    print("List:", numbers * 2)
    print("Tuple:", coordinates + (7, 8))
    print("Dictionary:", "name" in student)


if __name__ == "__main__":
    numbers = list(map(int, input("Enter list numbers separated by spaces: ").split()))

    coordinates = tuple(map(int, input("Enter tuple numbers separated by spaces: ").split()))

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))

    student = {"name": name, "age": age}