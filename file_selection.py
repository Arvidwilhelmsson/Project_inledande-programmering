import os
def file_selection():
    files_in_folder = os.listdir(".")
    
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

    found_name = None
    for name in files_in_folder:
        if name.lower() == file_choice_name.lower():
            found_name = name

    if found_name is None:
        print()
        print(f'Could not find "{file_choice_name}". Text files in this folder:')
        for name in files_in_folder:
            if name.lower().endswith(".txt"):
                print(f"  {name}")
        print()
        input("Press Enter to return to the file selection...")
        return file_selection()
    file_choice_name = found_name
    print()
      
    print(f"Analysing {file_choice_name}...")
    print()
    return file_choice_name
