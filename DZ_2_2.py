# Дан список:
#['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# Необходимо его обработать — обособить каждое целое число
# (вещественные не трогаем) кавычками (добавить кавычку до и кавычку
# после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
#['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

my_list = ['в', '5', 'часов', '17', 'минут',
           'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = []
for elem in my_list:
    if elem.isdigit():
        new_list.extend(['"', f'{int(elem):02}', '"'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
        new_list.extend(['"', f'{elem[0]}{int(elem[1:]):02}', '"'])
    else:
        new_list.append(elem)

out_info = ' '.join(new_list)
print(out_info)
