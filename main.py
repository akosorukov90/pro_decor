from logger_1 import logger_1
from logger_2 import param_logger


@logger_1
def print_name_1(name, prop=1):
    result = 'Ваше имя: ' + str(name)
    return result


@param_logger(param='debug_2.log')
def print_name_2(name, prop=1):
    result = 'Ваше имя: ' + str(name)
    return result


if __name__ == '__main__':
    print_name_1('Иван', prop=2)
    print_name_2('Петр', prop=3)
