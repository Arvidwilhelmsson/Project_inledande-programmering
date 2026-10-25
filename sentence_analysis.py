import matplotlib.pyplot as plt
def sentence_analysis(file):
    file.seek(0)

    sentence = ""
    number_words = 0
    previous_char = ""
    total_sentences = 0
    in_paragraph = False
    after_ellipsis = False
    sentence_lengths = []
    longest_sentence = ""
    shortest_sentence = None
    sentence_length_distribution = {}

    for line in file:
        line = line.replace("i.e.", "ie")
        words = line.lower().split()
        number_words += len(words)

        if line.split():
            if not in_paragraph:
                in_paragraph = True
        else:
            in_paragraph = False

        for char in line:
            if (char == ' ' and previous_char in ['.', '!', '?']) or (previous_char not in ['.', '!', '?'] and in_paragraph == False):
                total_sentences += 1

            sentence += char

            if char in ['.', '?', '!',':']:
                sentence = sentence.strip(" .!?")

                if char == '.' and previous_char == '.':
                    after_ellipsis = True

                if any(char.isalnum() for char in sentence):
                    length = len(sentence.split())

                if len(sentence.split()) > 1:
                    if len(sentence) > len(longest_sentence):
                        longest_sentence = sentence

                    if not after_ellipsis and (shortest_sentence is None or len(sentence) < len(shortest_sentence)):
                        shortest_sentence = sentence

                    if length in sentence_length_distribution:
                        sentence_length_distribution[length] += 1
                    else:
                        sentence_length_distribution[length] = 1

                if sentence != "":
                    after_ellipsis = False

                sentence = ""

            previous_char = char

    average_words_per_sentence = round(number_words / total_sentences, 1)

    print(f"Total sentences: {total_sentences:,}")
    print(f"Average words per sentence: {average_words_per_sentence:,}")
    print(f"Shortest sentence: {len(shortest_sentence.split())} words")
    print(f"Longest sentence: {len(longest_sentence.split())} words")
    print()
    print(f"Shortest sentence text: {shortest_sentence}")
    print(f"Longest sentence text: {longest_sentence}")
    print()
    print("Sentence length distribution (top 5):\n")
    print(f"Generating sentence analysis visualisation...\n")

    top_five = sorted(
        sentence_length_distribution.items(),
        key=lambda item: item[1],reverse=True)[:5]
    #items är nyckel och värde. key= lamda gör att item[1] är det som sorteras alltså antalet meningar. 
    # reverse=True tar från störst till minst och 5 är de 5 första.

    for item in top_five:
        print(f"  {item[0]} words: {item[1]} sentences")
    print()

    #Mathplotlib graphs
    for length, count in sentence_length_distribution.items():
        sentence_lengths.extend([length] * count)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.hist(sentence_lengths, bins=20, color='lightgreen',
             edgecolor='green')
    plt.title("Sentence Length Distribution")
    plt.xlabel("Sentence Length (words)")
    plt.ylabel("Frequency")

    plt.subplot(1, 2, 2)
    plt.bar([f"{length} words" for length, count in top_five], [count for length, count in top_five], color='orange')
    plt.title("Most Common Sentence Lengths")
    plt.xlabel("Sentence Length (words)")
    plt.ylabel("Number of Sentences")
    plt.xticks(rotation=45, ha='right')
    plt.show()