from write_func import write


def param_logger(param):
    def logger_2(func):
        def write_file(*args, **kwargs):
            result = func(*args, **kwargs)
            write(param, func.__name__, result, *args, **kwargs)
            return result
        return write_file
    return logger_2
