from write_func import write


def logger_1(func):
    def write_file(*args, **kwargs):
        result = func(*args, **kwargs)
        write('debug.log', func.__name__, result, *args, **kwargs)
        return result
    return write_file
