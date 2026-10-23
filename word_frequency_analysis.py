def word_frequency_analysis(file_name):

    file = open(file_name, 'r', encoding='utf-8')
    word_counts = {}
    unique_words = set()
    word_length = []
    for line in file:
        words = line.lower().split()
        for word in words:
            word = word.strip('/.|\'"*{[()}]?!%#€&=¶‰¢¥¡≠¿`^¨-_,;:·„≥>≤<@®¸√™“')
            if word:
                if word not in word_counts:
                    word_counts[word] = 1
                else:
                    word_counts[word] += 1
                unique_words.add(word)
                word_length.append(len(word))

    sett = set()
    for key, value in word_counts.items():
        sett.add((value, key))

    sett = sorted(sett, reverse=True)[0:10]
    
    counter = 0

    print("Top 10 most common words:")
    for number, word in sett:  
        counter += 1
        
        percentage = (number / len(word_length)) * 100 if word_length else 0
        print(f'{counter}. {word:<10} {number:,} times ({percentage:.1f}%)')

    shortest_word = min(word_length) if word_length else 0
    longest_word = max(word_length) if word_length else 0
    average_word_length = round(sum(word_length) / len(word_length), 1) if word_length else 0
    words_appearing_once = sum(1 for count in word_counts.values() if count == 1)
    
    print("\nWord length statistics:")
    print(f"  Shortest word: {shortest_word} characters")
    print(f"  Longest word: {longest_word} characters")
    print(f"  Average word length: {average_word_length} characters")
    print(f"Words appearing only once: {words_appearing_once:,}")

    file.close()
