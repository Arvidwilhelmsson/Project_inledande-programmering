def basic_statistics(file_name):
    file = open(file_name, 'r')

    lines = 0
    sentences = 0
    paragraphs = 0
    number_words = 0
    previous_char = ""
    unique_words = set()
    in_paragraph = False
    characters_with_spaces = 0
    characters_without_spaces = 0

    for line in file:
        words = line.lower().split()
        number_words += len(words)
        lines += 1

        for word in words:
            word = word.strip('/.|\'"*{[()}]?!%#€&=¶‰¢¥¡≠¿`^¨-_,;:·„≥>≤<@®¸√™“')
            unique_words.add(word)

        if line.split():
            if not in_paragraph:
                paragraphs += 1
                in_paragraph = True
        else:
            in_paragraph = False
        
        for char in line:
            if char in [' '] and previous_char in ['.','!','?'] or previous_char not in ['.','!','?'] and in_paragraph == False:
                sentences += 1
            previous_char = char


        characters_with_spaces += len(line)
        characters_without_spaces += len(line.replace(' ', ''))

    words_per_line = round(number_words/lines, 1)
    average_word_length = round(characters_without_spaces / number_words, 1)
    average_words_per_sentence = round(number_words / sentences, 1)

    print(f"Lines: {lines:,}")
    print(f"Paragraphs: {paragraphs:,}")
    print(f"Sentences: {sentences:,}")
    print(f"Words: {number_words:,}")
    print(f"Unique words: {len(unique_words):,}")
    print(f"Characters (with spaces): {characters_with_spaces:,}")
    print(f"Characters (without spaces): {characters_without_spaces:,}")
    print(f"Average words per line: {words_per_line}")
    print(f"Average word length: {average_word_length} characters")
    print(f"Average words per sentence: {average_words_per_sentence}")
    print()

    #print("Generating basic statistics visualisation...")
    #print()
    #print("Press Enter to continue...")
    file.close()