while True:
    print("\n--- Menu ---")
    print("1. Word occurrence")
    print("2. Character frequency")
    print("3. Factors of a number")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice ==  1:
        text = input("Enter a line of text: "))
        words = text.split()
        word_coun t= {}
        for w in words:
           word_count[word]=word_count.get(word, 0) + 1
        print("word occurrences:",word_count)
     elif choice =={}
       for word in word:
            word_count{word} =word
        for word, count in word_count.items():
            print(f"'{word}': {count}")
        print()
    
    elif choice == '2':
        # Option 2: Character frequency
        text = input("Enter a string: ")
        frequency = {}
        for char in text:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        print("Character frequencies:")
        for char, count in frequency.items():
            print(f"'{char}': {count}")
            
    elif choice == '3':
        # Option 3: Factors of a number
        try:
            num = int(input("Enter a positive integer: "))
            if num <= 0:
                print("Please enter a positive integer.")
                continue

            factors = []
            for i in range(1, num + 1):
                if num % i == 0:
                    factors.append(i)
            print(f"The factors of {num} are: {factors}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
    elif choice == '4':
        # Option 4: Exit
        print("Exiting program.")
        break
        
    else:
        # Invalid choice handling
        print("Invalid choice. Please enter a number between 1 and 4.")
