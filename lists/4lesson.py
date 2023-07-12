# СПИСКИ

names = ['foma', 'stepa', 'baby', 'demon', 'cube', 'leha']
print(names[-1].title()) # последний элемент списка

names[0] = 'sasha' # замена первого элемента списка
print(names[0].title()) # первый элемент списка

names.append('abc') # добавление в конец списка еще одного элемента
print(names)

names.insert(0, 'zxy') # добавление в рандомное место нового элемента списка (сам определяешь место, куда данный символ должен вставляться)
print(names)

del names [0] # удаление элемента по порядковому номеру из спика
print(names)

delited_name = names.pop() # удаляет последний элемент списка по дефолту, если оставить () пустым значением
print(delited_name)
print(names)

delited_name_1 = names.pop(0) # удаляет первый элемнт
print(delited_name_1)
print(names)

remove_name = 'baby' # загоняет в новую переменную удаляемое значение
names.remove(remove_name) # удаляет это значение из списка
print(remove_name)
print(names)

names.sort() # сортирвка в алфовитном порядке. ВЕРНУТЬ В ИСХОДНОЕ ПОЛОЖЕНИЕ УЖЕ НЕЛЬЗЯ
print(f"{names}")
names.sort(reverse=True) # сортирвка в обратном алфовитном порядке. ВЕРНУТЬ В ИСХОДНОЕ ПОЛОЖЕНИЕ УЖЕ НЕЛЬЗЯ
# видимо поэтому этот метод нельзя сразу использовать в print, потому что мы присваеваем новое значение переменной
print(f"{names}")

names2 = ['foma', 'stepa', 'baby', 'demon', 'cube', 'leha']
print(sorted(names2)) # временная сортировка в алфовитном порядке. МОЖНО ВЕРНУТЬ В ИСХОДНОЕ ПОЛОЖЕНИЕ
print(names2) # убеждаемся, что сортировка является временной
print(sorted(names2, reverse=True)) # сортирвка в обратном алфовитном порядке

names2.reverse() # записывает списко в обратном порядке (с конца)
print(names2)
names2.reverse() # возвращает в обратное положение
print(names2)

print(len(names2)) # определяет длину списка


