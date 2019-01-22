# files & directories
def file_true(file_name):
    from os.path import isfile
    return isfile(file_name)


def file_false(file_name):
    from os.path import isfile
    return not isfile(file_name)


def dir_true(file_name):
    from os.path import isdir
    return isdir(file_name)


def dir_false(file_name):
    from os.path import isdir
    return not isdir(file_name)


def file_r_true(file_name):
    from os import access, R_OK
    return access(file_name, R_OK)


def file_r_false(file_name):
    from os import access, R_OK
    return not access(file_name, R_OK)


def file_w_true(file_name):
    from os import access, W_OK
    return access(file_name, W_OK)


def file_w_false(file_name):
    from os import access, W_OK
    return not access(file_name, W_OK)


def file_x_true(file_name):
    from os import access, X_OK
    return access(file_name, X_OK)


def file_x_false(file_name):
    from os import access, X_OK
    return not access(file_name, X_OK)

