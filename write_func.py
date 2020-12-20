import datetime
import json


def write(path, name, result, *args, **kwargs):
    with open(path, 'a') as f:
        now = datetime.datetime.now()
        now_dt = now.strftime("%d.%m.%Y-%H:%M:%S")
        arguments = ''
        for arg in args:
            if type(arg) == list:
                for child_arg in arg:
                    arguments = arguments + str(child_arg) + ', '
            else:
                arguments = arguments + str(arg) + ', '
        for key, value in kwargs.items():
            arguments = arguments + key + ': ' + str(value) + ', '
        if type(result) == dict:
            output = json.dumps(result)
        else:
            output = result
        f.write('Дата вызова: ' + now_dt + '\n')
        f.write('Имя функции: ' + name + '\n')
        f.write('Аргументы: ' + arguments + '\n')
        f.write('Результат функции: ' + output + '\n\n')