def character_analysis(file_name):
    file = open(file_name, 'r')


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

    file.close()