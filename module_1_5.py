immutable_var = ('My_name', 'Artur', 123, True, 1.6)
print(immutable_var)
# изменить элементы кортежа невозможно, т.к. кортеж не поддерживает обращение по элементам
mutable_list = ([1, 2, 3, 4, 5], 'начинаю мотылять')
print(mutable_list)
mutable_list[0][0] = 'раз'
mutable_list[0][1] = 'два'
mutable_list[0][2] = 'три'
mutable_list[0][3] = 'четыре'
mutable_list[0][4] = 'пять'
print(mutable_list)