immutable_var = 3, 'boxes of', ['apples', 'bananas', 'potatoes'], True
print('Immutable tuple:', immutable_var)
# immutable_var[0] = 5 # => в консоли вывода выводится ошибка:
# TypeError: 'tuple' object does not support item assignment, или
# TypeError: объект 'tuple' не поддерживает назначение элементов
# Кортеж – это неизменяемая упорядоченная коллекция, или неизменяемый объект, элементы которого мы не можем изменять.
mutable_list = [3, 'boxes of', ['apples', 'bananas', 'potatoes'], True]
mutable_list[0] = 5
mutable_list[1] = 'ящиков'
mutable_list[2][2] = 'peaches'
mutable_list.remove(True)
mutable_list.append('и')
mutable_list.extend([7, 'ящиков', 'pears'])
print('Mutable list:', mutable_list)