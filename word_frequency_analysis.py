def word_frequency_analysis(file_name):
    word_counts = {}
    word_length = []
    number_words = 0
    characters_without_spaces = 0

    punctuation = '.,!?"\'()[]{}:;-_'
    table = str.maketrans('', '', punctuation)

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.lower().split()
            number_words += len(words)
            characters_without_spaces += len(line.replace(' ', ''))
            for word in words:
                word = word.translate(table)
                if word:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
                    word_length.append(len(word))

    total_words = len(word_length)

    print("Top 10 most common words:")
    flipped_list = []
    for word, count in word_counts.items():
        flipped_list.append((count, word))

    sorted_words = sorted(flipped_list, reverse=True)
    for count, word in sorted_words[:10]:
        percentage = count / total_words * 100 if total_words else 0
        print(f'{word:<10} {count:,} times ({percentage:.1f}%)')

    shortest_word = min(word_length) if word_length else 0
    longest_word = max(word_length) if word_length else 0
    average_word_length = round(characters_without_spaces / number_words, 1) if number_words else 0
    words_appearing_once = 0
    for count in word_counts.values():
        if count == 1:
            words_appearing_once += 1

    print("\nWord length statistics:")
    print(f"  Shortest word: {shortest_word} characters")
    print(f"  Longest word: {longest_word} characters")
    print(f"  Average word length: {average_word_length} characters")
    print(f"Words appearing only once: {words_appearing_once:,}")