def character_analysis(file_name):
    file = open(file_name, 'r')

    word_length = []
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
                word_length.append(char)
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
        percentage_letters = (number/len(word_length)) * 100
        print(f'  {counter:>2} {repr(char)} - {number:,} times ({round(percentage_letters,1)}%)')

    file.close()
