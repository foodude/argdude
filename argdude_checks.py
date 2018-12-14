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



# users & group 
def get_user_list(user_type):
    user_types = {'user_name' : 0, 'user_id' : 2}
    with open('/etc/passwd', 'r') as file:
        return [x.split(':')[user_types[user_type]] for x in file]


def get_group_list(group_type):
    group_types = {'group_name' : 0, 'group_id' : 2}
    with open('/etc/group', 'r') as file:
        return [x.split(':')[group_types][group_type] for x in file]


def user_name_true(user_name):
    return user_name in get_user_list('user_name')


def user_name_false(user_name):
    return user_name not in get_user_list('user_name')


def user_id_true(user_id):
    return user_id in get_user_list('user_id')


def user_id_false(user_id):
    return user_id not in get_user_list('user_id')


def group_name_true(group_name):
    return group_name in get_group_list('group_name')


def group_name_false(group_name):
    return group_name not in get_group_list('group_name')


def group_id_true(group_id):
    return group_id in get_group_list('group_id')


def group_id_false(group_id):
    return group_id not in get_group_list('group_id')



## network interfaces
def get_iface_list():
    with open('/proc/net/dev', 'r') as file:
        return [x.split(' ')[0][0:-1] for x in file if x.split(' ')[0]][1:]

def iface_name_true(iface_name):
    return iface_name in get_iface_list()

def iface_name_false(iface_name):
    return iface_name not in get_iface_list()

