# Вывести последнюю букву в слове
word = 'Архангельск'
lenght_of_word = len(word)
print(f"Last char of word '{word}' is '{word[lenght_of_word - 1]}'.")

# Вывести количество букв "а" в слове
word = 'Архангельск'
count_chars = word.lower().count("а")
print(f"Word '{word.lower()}' has {count_chars} chars 'a'.")

# Вывести количество гласных букв в слове
word = 'Архангельск'
word = word.lower()
vowels = ["а", "о", "э", "и", "у", "ы", "е", "ё", "ю", "я"]
vowel_count = 0
for i in range(len(word)):
    if word[i] in vowels:
        vowel_count += 1
print(f"Word '{word}' has {vowel_count} vowels.")

# Вывести количество слов в предложении
sentence = "Мы приехали в гости"
splited_sen = sentence.split()
ammount_of_words = len(splited_sen)
print(f"Sentence '{sentence}' has {ammount_of_words} words.")

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print(f"First chars of each word from sentence '{sentence}' are:")
splited_sen = sentence.split()
for i in range(len(splited_sen)):
    print(splited_sen[i][0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
splited_sen = sentence.split()
mean_length = 0
for i in range(len(splited_sen)):
    mean_length += len(splited_sen[i])
mean_length /= len(splited_sen)
print(f"Mean length is {int(mean_length)}.")