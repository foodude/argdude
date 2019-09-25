# files & directories
from os.path import isfile, isdir
from os import access, R_OK, W_OK, X_OK


def file_true(file_name):
    return isfile(file_name)


def file_false(file_name):
    return not isfile(file_name)


def dir_true(file_name):
    return isdir(file_name)


def dir_false(file_name):
    return not isdir(file_name)


def file_r_true(file_name):
    return access(file_name, R_OK)


def file_r_false(file_name):
    return not access(file_name, R_OK)


def file_w_true(file_name):
    return access(file_name, W_OK)


def file_w_false(file_name):
    return not access(file_name, W_OK)


def file_x_true(file_name):
    return access(file_name, X_OK)


def file_x_false(file_name):
    return not access(file_name, X_OK)
