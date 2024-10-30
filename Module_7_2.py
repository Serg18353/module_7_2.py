def custom_write(file_name: str, string: list):

    string_position = {}
    n_str = 1
    file = open(file_name, 'w')

    for str in string:
        n_bytes = file.tell()
        file.write(f'{str}')
        file.write('\n')

        string_position[(n_str,n_bytes)]  = str
        n_str += 1
    file.close()
    return string_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)