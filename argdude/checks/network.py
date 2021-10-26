""" argdude network interface tests """


def get_iface_list():
    """ return network devices from /proc """
    with open('/proc/net/dev', 'r') as file:
        return [x.split(':')[0].strip()
                for x in file if len(x.split(':')) > 1]


def iface_name_true(iface_name):
    """ check if a network interface exist """
    return iface_name['kw_value'] in get_iface_list()


def iface_name_false(iface_name):
    """ check if a network interface does not exist """
    return iface_name['kw_value'] not in get_iface_list()

