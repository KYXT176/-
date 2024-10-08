def print_params (a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = [5, 'новый текст', False]
values_dict = {"a": 1, "b": 2, "c": 3}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)