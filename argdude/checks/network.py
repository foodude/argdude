## network interfaces
def get_iface_list():
    with open('/proc/net/dev', 'r') as file:
        return [x.split(' ')[0][0:-1] for x in file if x.split(' ')[0]][1:]

def iface_name_true(iface_name):
    return iface_name in get_iface_list()

def iface_name_false(iface_name):
    return iface_name not in get_iface_list()

