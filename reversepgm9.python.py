def reverse_number(num):
    num_str = str(num)
    reversed_str = ""
    for i in range(len(num_str) - 1, -1, -1):
        reversed_str += num_str[i]
    return int(reversed_str)

def read_number():
    number = int(input("Enter a number (at least 4 digits): "))
    while number < 1000:
        print("Please enter a number with at least 4 digits.")
        number = int(input("Enter a number (at least 4 digits): "))
    return number

def main():
    number = read_number()
    reversed_num = reverse_number(number)
    print("Original number:", number)
    print("Reversed number:", reversed_num)

main()
