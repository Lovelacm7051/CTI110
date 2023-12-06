def main():
    first_integer = int(input())
    second_integer = int(input())

    current_value = first_integer
    while current_value <= second_integer:
        print(current_value, end=' ')
        current_value += 5

    print()  # Add a newline after the sequence

if __name__ == "__main__":
    main()