# users & group 
def get_user_list(user_type):
    user_types = {'user_name' : 0, 'user_id' : 2}
    with open('/etc/passwd', 'r') as file:
        return [x.split(':')[user_types[user_type]] for x in file]


def get_group_list(group_type):
    group_types = {'group_name' : 0, 'group_id' : 2}
    with open('/etc/group', 'r') as file:
        return [x.split(':')[group_types[group_type]] for x in file]


def user_name_true(user_name):
    return user_name in get_user_list('user_name')


def user_name_false(user_name):
    return user_name not in get_user_list('user_name')


def user_id_true(user_id):
    return str(user_id) in get_user_list('user_id')


def user_id_false(user_id):
    return str(user_id) not in get_user_list('user_id')


def group_name_true(group_name):
    return group_name in get_group_list('group_name')


def group_name_false(group_name):
    return group_name not in get_group_list('group_name')


def group_id_true(group_id):
    return group_id in get_group_list('group_id')


def group_id_false(group_id):
    return group_id not in get_group_list('group_id')

