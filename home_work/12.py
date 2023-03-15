#При помощи функции filter() из котрежа слов отфильтровать только те, которые являются полиндромами
#(слова которые читаются одинаково в обе стороны), регистр букв не учитывать.
inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']


def inputdata_01(word):
    word = word.lower()
    return word == word[::-1]


result = list(filter(lambda x: inputdata_01(x), inputdata))
print(result)
