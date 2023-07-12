# Упражнения
# 3.4
guests = ['foma', 'vlad kub', 'vlad demon', 'leha', 'baby']
print(f"Привет, {guests[0].title()}, {guests[1].title()}, {guests[2].title()}, {guests[3].title()}, {guests[4].title()}. Сегодня я хочу пригласить вас на свой ДР!")

print(f"\nВот твое приглашение, {guests[0].title()}. Добро пожаловать!")
print(f"\nВот твое приглашение, {guests[1].title()}. Добро пожаловать!")
print(f"\nВот твое приглашение, {guests[2].title()}. Добро пожаловать!")
print(f"\nВот твое приглашение, {guests[3].title()}. Добро пожаловать!")
print(f"\nВот твое приглашение, {guests[4].title()}. Добро пожаловать!")

# 3.5
epsent = 'baby'
guests.remove(epsent)
print(f"\n{epsent.title()} не смог прийти из-за того, что Гелик его съел")

guests.append('artem')
print(f"\nПривет, {guests[0].title()}, {guests[1].title()}, {guests[2].title()}, {guests[3].title()}, {guests[4].title()}. Список гостей был изменен")

print(f"\nВот твое приглашение, {guests[0].title()}. Добро пожаловать!")
print(f"\nВот твое приглашение, {guests[1].title()}. Добро пожаловать!")
print(f"\nВот твое приглашение, {guests[2].title()}. Добро пожаловать!")
print(f"\nВот твое приглашение, {guests[3].title()}. Добро пожаловать!")
print(f"\nВот твое приглашение, {guests[4].title()}. Добро пожаловать!")

#3.6
print("\nВ честь того, что я купил новый стол, я приглашаю еще несколько друзей, встречайте!")
guests.insert(0, 'danila')
guests.insert(3, 'oleg')
guests.append('arseniy')
print(f"\nПоздоровайтесь с новобранцами! вот ваши приглашения: \nВот твое приглашение, {guests[0].title()}. Добро пожаловать! \nВот твое приглашение, {guests[1].title()}. Добро пожаловать! \nВот твое приглашение, {guests[2].title()}. Добро пожаловать! \nВот твое приглашение, {guests[3].title()}. Добро пожаловать! \nВот твое приглашение, {guests[4].title()}. Добро пожаловать! \nВот твое приглашение, {guests[5].title()}. Добро пожаловать! \nВот твое приглашение, {guests[6].title()}. Добро пожаловать! \nВот твое приглашение, {guests[7].title()}. Добро пожаловать!")

#3.7
print("\nПиздец, сказали, что стол не привезут, а диван спиздили. Ко мне можно только 2х человек.")

a = guests.pop(0)
b = guests.pop(1)
c = guests.pop(2)
b = guests.pop(3)
d = guests.pop(-1)
e = guests.pop(-3) # почему-то фома для списка это -3

print(f"\nДля тебя все отсается в силе, {guests[0].title()}. Добро пожаловать! \nДля тебя все отсается в силе, {guests[1].title()}. Добро пожаловать!")

del guests[0]
del guests[-1]
print(guests)