play_word_list = []
with open("files/word_rus.txt") as file:
    base_word_list = [row.strip() for row in file]
input_word = ''
bot_answer = ''
print('Ведите слово:')

while input_word.lower() != 'конец игры':
    input_word = input()
    if input_word.lower() == 'конец игры':
        break

    while input_word.lower() not in base_word_list:
        print("Такого слова не существует, либо я его не знаю =)\n"
              "Введите слово ещё раз:")
        input_word = input()
        if input_word.lower() == 'конец игры':
            break

    while input_word.lower() in play_word_list:
        print("Это слово уже было, давай другое:")
        input_word = input()
        if input_word.lower() == 'конец игры':
            break

    if input_word.lower() == 'конец игры':
        break

    play_word_list.append(input_word)
    base_word_list.remove(input_word)

    for find_word in base_word_list:
        if len(find_word) > 2:
            last_letter = play_word_list[-1][-1]
            if last_letter == 'ь' or last_letter == 'ъ' or last_letter == 'ы':
                last_letter = play_word_list[-1][-2]

            if last_letter == find_word[0] and find_word not in play_word_list:
                bot_answer = find_word
                base_word_list.remove(find_word)
                break
    else:
        print('я проиграл...')
        input_word = 'конец игры'
        print(play_word_list)
        print(base_word_list)

    play_word_list.append(bot_answer)
    print(bot_answer)
