import datetime


def write(path, name, result, *args, **kwargs):
    with open(path, 'a') as f:
        now = datetime.datetime.now()
        now_dt = now.strftime("%d.%m.%Y-%H:%M:%S")
        arguments = ''
        for arg in args:
            arguments = arguments + arg + ', '
        for key, value in kwargs.items():
            arguments = arguments + key + ': ' + str(value) + ', '
        f.write('Дата вызова: ' + now_dt + '\n')
        f.write('Имя функции: ' + name + '\n')
        f.write('Аргументы: ' + arguments + '\n')
        f.write('Результат функции: ' + result + '\n\n')