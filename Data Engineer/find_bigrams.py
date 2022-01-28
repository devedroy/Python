sentence = """
Have free hours and love children?
Drive kids to school, soccer practice
and other activities."""

def find_bigrams(sentence):
    input_list = sentence.split()
    bigrams_list = []

    for i in range(len(input_list)-1):
        bigrams_list.append((input_list[i].strip().lower(), input_list[i+1].strip().lower()))

    return bigrams_list

print(find_bigrams(sentence))