
def custom_write(file_name, strings):
    str_point = 0
    strings = {}
    for i in info:
        file = open(file_name, 'a', encoding='utf-8')
        tell = (file.tell())
        str_point += 1
        file.write(f'{i}\n')
        file.close()
        strings.update({(str_point,tell): i})
    return strings

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)


