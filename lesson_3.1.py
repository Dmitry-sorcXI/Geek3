translation = {"Dance": "Танец" , "Table": "Стол", "Hand": "Ладонь", "France": "Франция" , "TV": "Телевизор" , "Donut": "Пончик", "Song": "Песня", "Girl": "Девочка", "Mafia": "Мафия" }

def num_translation(word):
    return translation.get(word)

print(num_translation(input("Введите слово для перевода: ")))