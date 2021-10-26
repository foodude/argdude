from os.path import isfile, isdir
from os import access, R_OK, W_OK, X_OK


def file_true(file_name):
    return isfile(file_name['kw_value'])


def file_false(file_name):
    return not isfile(file_name['kw_value'])


def dir_true(file_name):
    return isdir(file_name['kw_value'])


def dir_false(file_name):
    return not isdir(file_name['kw_value'])


def file_r_true(file_name):
    return access(file_name['kw_value'], R_OK)


def file_r_false(file_name):
    return not access(file_name['kw_value'], R_OK)


def file_w_true(file_name):
    return access(file_name['kw_value'], W_OK)


def file_w_false(file_name):
    return not access(file_name['kw_value'], W_OK)


def file_x_true(file_name):
    return access(file_name['kw_value'], X_OK)


def file_x_false(file_name):
    return not access(file_name['kw_value'], X_OK)
