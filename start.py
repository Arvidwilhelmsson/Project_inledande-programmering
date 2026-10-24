#import matplotlib.pyplot as plt
from basic_statistics import basic_statistics
from sentence_analysis import sentence_analysis
from word_frequency_analysis import word_frequency_analysis
from file_selection import file_selection
from character_analysis import character_analysis
def main():
    choice = None
    loaded_file = None
    file_choice_name = None
    fil = ["A Doll's House_Henrik Ibsent", "Frankenstein by Mary Wollstonecraft Shelley", "Moby-Dick_Herman Melville", "The Red Room August Strindberg", "The Time Machine by H. G. Wells", "Crime_and_punishment.txt"]
    print(f"Welcome to the Text analyser!\nThis program analyses text files and provies statistical insights.\n\n")

    while True:
        # 1. Huvudmeny
        print("="*60)
        print(" "*20, end='')
        print("TEXT ANALYSER")
        print("="*60)
        print("1. Load text file")
        print("2. Display basic statistics")
        print("3. Word frequency analysis")
        print("4. Sentence analysis")
        print("5. Character analysis")
        print("6. Export results")     
        print("7. Exit")
        print("="*60)
        

        # Visa status för laddad fil
        if file_choice_name is None:
            print("No file loaded")
        else:
            print(f"Current file: {file_choice_name}")
        print("="*60)
        print()


        # 2. Läs in menyval
        choice = input("Enter your choice (1-7): ").strip(" ")
        

        if choice in ["2", "3", "4", "5", "6"] and file_choice_name is None:
            print("="*60)
            print("Please load a file first!")
            print("="*60)
            print(f"\n"*5)
            continue
                
        # 3. Hantera valet
        elif choice == "1":
            print("\n--- File selection ---")
            file_choice_name = file_selection()
            print()

        elif choice == "2":
            print()
            print(f"--- Basic Statistics for {file_choice_name} ---")
            basic_statistics(file_choice_name)
            print(f"\n"*2)

        elif choice == "3":
            print(f"--- Word Analysis for {file_choice_name} ---")
            word_frequency_analysis(file_choice_name)
            print(f"\n"*2)

        elif choice == "4":
            print()
            print(f"--- Sentence Analysis for {file_choice_name} ---")
            sentence_analysis(file_choice_name)
            print(f"\n"*2)

        elif choice == "5":
            print()
            print(f"--- Character Analysis for {file_choice_name} ---")
            character_analysis(file_choice_name)
            print(f"\n"*2)

        elif choice == "6":
            print()
            print("Export results")
            print(f"\n"*2)

        elif choice == "7":
            print(f"\n"*2)
            print("Thank you for using Text analyser!")
            print()
            break #Stänger loopen och avslutar programmet

        else:
            print()
            print("Måste vara mellan 1-7")
            print()
main()

