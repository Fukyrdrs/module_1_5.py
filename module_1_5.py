immutable_var = 'table', 12, True
print('Immutable tuple:', immutable_var)
#immutable_var[1] = 21  Изменить кортеж нельзя, потому что кортеж не поддерживает обращение по элементам
mutable_list = ['table', 12, True]
mutable_list[0] = 'chair'
mutable_list[1] = 221
mutable_list[2] = False
print('Mutable list:', mutable_list)
