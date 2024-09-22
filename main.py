None
meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РОФЛ": "шутка"
            }
while True:
    vopr = input("Что сделать?")
    if vopr == "Добавить" or vopr == "1":
        a = input("Слово")
        b = input("Значение")
        meme_dict[a] = b
    elif vopr == "Удалить" or vopr == "2":
        a = input("Слово")
        a = a.upper()
        del meme_dict[a]
    else:
        print()
    for i in meme_dict.keys():
        print(i)
    word = input("Введите непонятное слово (большими буквами!): ")
    word = word.upper()
    if word in meme_dict.keys():
        # Что делать, если слово нашлось?
        print(meme_dict[word])
        print("")
    else:
        # Что делать, если слово не нашлось?
        print("Такого слова нет")
        print("")
