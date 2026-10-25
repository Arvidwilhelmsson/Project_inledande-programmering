def file_selection():
    
    print("Available text files:")
    print("1. A Doll's House_Henrik Ibsent.txt")
    print("2. Frankenstein bu Mary Wollstonecraft Shelley.txt")
    print("3. Moby-Dick_Herman Melville.txt")
    print("4. The Red Room_August Strindberg.txt")
    print("5. The Time Machine by H. G. Wells.txt")
    print("6. Crime_and_punishment.txt")
    print()

    file_choice = input("Enter filename or number from list above: ").strip()
    if file_choice == "1":
        file_choice_name = "A Doll's House_Henrik Ibsen.txt"
    elif file_choice == "2":
        file_choice_name = "Frankenstein by Mary Wollstonecraft Shelley.txt"
    elif file_choice == "3":
        file_choice_name = "Moby-Dick_Herman Melville.txt"
    elif file_choice == "4":
        file_choice_name = "The Red Room_August Strindberg.txt"
    elif file_choice == "5":
        file_choice_name = "The Time Machine by H. G. Wells.txt"
    elif file_choice == "6":
            file_choice_name = "Crime_and_punishment.txt"
    else:
        file_choice_name = file_choice
        if not file_choice_name.lower().endswith(".txt"):
            file_choice_name += ".txt"
    print()
    
    print(f"Analysing {file_choice_name}...")
    print()
    return file_choice_name
