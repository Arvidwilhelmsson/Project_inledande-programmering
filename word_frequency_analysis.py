import matplotlib.pyplot as plt
def word_frequency_analysis(file_lines):

    counter = 0
    word_counts = {}
    word_length = []
    number_words = 0
    flipped_list = []
    words_appearing_once = 0
    characters_without_spaces = 0
    punctuation = '.,!?"\'()[]{}:;-_'

    for line in file_lines:
        words = line.lower().split()
        number_words += len(words)
        characters_without_spaces += len(line.replace(' ', ''))

        for word in words:
            new_word = ""
            for char in word:
                if char not in punctuation:
                    new_word += char
            word = new_word

            if word:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
                word_length.append(len(word))

    total_words = len(word_length)
    shortest_word = min(word_length) if word_length else 0
    longest_word = max(word_length) if word_length else 0
    average_word_length = round(characters_without_spaces / number_words, 1) if number_words else 0

    print("Top 10 most common words:")
    for word, count in word_counts.items():
        flipped_list.append((count, word))

    for count, word in sorted(flipped_list, reverse=True)[:10]:
        counter += 1
        percentage = count / total_words * 100 if total_words else 0
        print(f'  {counter:>2}. {word:<16} {count:,} times ({percentage:.1f}%)')

    for count in word_counts.values():
        if count == 1:
            words_appearing_once += 1

    print("\nWord length statistics:")
    print(f"  Shortest word: {shortest_word} characters")
    print(f"  Longest word: {longest_word} characters")
    print(f"  Average word length: {average_word_length} characters")
    print(f"Words appearing only once: {words_appearing_once:,}")

    #Mathplotlib graphs
    top_words = sorted(flipped_list, reverse=True)[:10]
    word_labels = [word for count, word in top_words]
    word_values = [count for count, word in top_words]

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.bar(word_labels, word_values, color='skyblue', edgecolor='blue')
    plt.title("Top 10 Most Common Words")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45, ha='right')

    plt.subplot(1, 2, 2)
    plt.hist(word_length, bins=range(1, max(word_length) + 2),
             color='lightcoral', edgecolor='red')
    plt.title("Word Length Distribution")
    plt.xlabel("Word Length (characters)")
    plt.ylabel("Frequency")
    plt.show()