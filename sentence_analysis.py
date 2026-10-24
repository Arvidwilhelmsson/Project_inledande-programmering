def sentence_analysis(file_lines):

    sentence = ""
    number_words = 0
    previous_char = ""
    total_sentences = 0
    in_paragraph = False
    longest_sentence = ""
    shortest_sentence = None
    sentence_length_distribution = {}

    for line in file_lines:
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

                if any(char.isalnum() for char in sentence):
                    length = len(sentence.split())

                if len(sentence.split()) > 1:
                    if len(sentence) > len(longest_sentence):
                        longest_sentence = sentence

                    if shortest_sentence is None or len(sentence) < len(shortest_sentence):
                        shortest_sentence = sentence

                    if length in sentence_length_distribution:
                        sentence_length_distribution[length] += 1
                    else:
                        sentence_length_distribution[length] = 1

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
    print("Sentence length distribution (top 5):")

    top_five = sorted(
        sentence_length_distribution.items(),
        key=lambda item: item[1],reverse=True)[:5]
    #items är nyckel och värde. key= lamda gör att item[1] är det som sorteras alltså antalet meningar. 
    # reverse=True tar från störst till minst och 5 är de 5 första.

    for item in top_five:
        print(f"  {item[0]} words: {item[1]} sentences")

    print()
    
    #print("Generating sentence analysis visualisation...")
    #print()
    #print("Press Enter to continue...")