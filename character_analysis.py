import matplotlib.pyplot as plt
def character_analysis(file):
    file.seek(0)

    word_counts = {}
    spaces = 0
    letters = 0
    digits = 0
    number_punctuations = 0
    punctuation = '/.|\'"*{[()}]?!%#€&=¶‰¢¥¡≠¿`^¨-_,;:·„≥>≤<@®¸√™'
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for line in file:
        characters = line.lower()
        for char in characters:
            if char in alphabet:
                letters += 1
                if char not in word_counts:
                    word_counts[char] = 1
                else:
                    word_counts[char] += 1
            elif char == " ":
                spaces += 1
            elif char.isdigit() == True:
                digits += 1
            elif char in punctuation:
                number_punctuations += 1


    sett = set()
    for key, value in word_counts.items():
        sett.add((value, key))
    sett = sorted(sett, reverse=True)[0:10]
    total = letters + digits + spaces + number_punctuations

    print("Character type distribution:")
    print(f'  Letters: {letters:,} ({round(letters / total * 100, 1)}%)')
    print(f'  Digits: {digits:,} ({round(digits / total * 100, 1)}%)')
    print(f'  Spaces: {spaces:,} ({round(spaces / total * 100, 1)}%)')
    print(f'  Punctuation: {number_punctuations:,} ({round(number_punctuations / total * 100, 1)}%)')
    print()
    print("Most common letters:")
    counter = 0
    for number, char in sett:
        counter += 1
        percentage_letters = (number/letters) * 100
        print(f'  {counter:>2} {repr(char)} - {number:,} times ({round(percentage_letters,1)}%)')
    print()
    print(f"Generating character analysis visualisation...\n")

    #Mathplotlib graphs
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.bar([char for number, char in sett], [number for number, char in sett], color='purple')
    plt.title("Top 10 Most Common Letters")
    plt.xlabel("Letters")
    plt.ylabel("Frequency")

    plt.subplot(1, 2, 2)
    labels = ["Letters", "Spaces", "Punctuation"]
    values = [letters, spaces, number_punctuations]
    
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("Character Type Distribution")
    plt.show()