""" description """

import logging as log
log.getLogger().addHandler(log.NullHandler())


def initialize(chk_args):
    """ initialyze chk_args """

    def stupid():
        return None

    keys = {'opt_required'     : [bool, type],
            'opt_required_bool': [bool, type],
            'opt_include'      : [list],
            'opt_exclude'      : [list],
            'opt_set_var'      : [dict],
            'arg_type'         : [list],
            'arg_etype'        : [list],
            'char_min'         : [int],
            'char_max'         : [int],
            'int_min'          : [int],
            'int_max'          : [int],
            'float_min'        : [float],
            'float_max'        : [float],
            'decp_min'         : [int],
            'decp_max'         : [int],
            'list_min'         : [int],
            'list_max'         : [int],
            'arg_allow'        : [list],
            'arg_deny'         : [list],
            'arg_check'        : [type(stupid), list],
            'arg_default'      : [type(stupid),
                                  bool, str, int, float, list, dict, tuple],
            'set_var'          : [dict],
            'sys_arg'          : [list]}

    for option_name in chk_args:
        for chk_args_keyword in chk_args[option_name]:
            if chk_args_keyword == 'arg_default':
                continue

            if chk_args_keyword not in keys:
                log.error('chk_args: keyword does not exist! ( %s )',
                          chk_args_keyword)
                return False

            if not isinstance(chk_args[option_name][chk_args_keyword],
                              tuple(keys[chk_args_keyword])):
                log.error('chk_args, [%s]: key value has wrong type! '
                          '( %s != %s )',
                          chk_args_keyword,
                          type(chk_args[option_name][chk_args_keyword]),
                          keys[chk_args_keyword])
                return False
    return True


def opt_unknown(args, chk_args):
    """
    check if a arg in args does not
    exist in chk_args
    """
    for option_name in args:
        if option_name not in chk_args:
            if option_name == 'opt_ignore':
                continue

            log.error('opt: unknown option! ( %s )', option_name)
            return False

    return True


def opt_ignore(args, chk_args):
    """ check if an arg should be ignored """

    if 'opt_ignore' not in args:
        return chk_args

    for option_name in args['opt_ignore']:
        if option_name in chk_args:
            log.debug('opt: ignore option! ( %s )', option_name)
            chk_args.pop(option_name)

    return chk_args


def opt_required(args, chk_args):
    """ check if all required arguments in args """

    for option_name in chk_args:
        if 'opt_required' not in chk_args[option_name]:
            continue

        if chk_args[option_name]['opt_required'] is True:
            if option_name not in args:
                log.error('opt: is required but undefined! ( %s )',
                          option_name)
                return False

    return True


def opt_required_bool(args, chk_args):
    """
    check if one of required_bool arguments
    is in args
    """
    required_bool = []
    for option_name in chk_args:
        if 'opt_required' not in chk_args[option_name]:
            continue

        if chk_args[option_name]['opt_required'] is bool:
            required_bool.append(option_name)

    for option_name in required_bool:
        if option_name in args:
            return True

        log.error('opt [%s]: expect one option but none is defined! ( %s )',
                  option_name,
                  str(required_bool))
        return False

    return True


def opt_include(args, chk_args):
    """ check if opt_include arguments in args """

    for option_name in chk_args:
        if 'opt_include' not in chk_args[option_name]:
            continue

        if option_name not in args:
            continue

        for include_option in chk_args[option_name]['opt_include']:
            if include_option not in args:
                log.error('opt, [%s]: depends on option! ( %s )',
                          option_name,
                          include_option)
                return False

    return True


def opt_exclude(args, chk_args):
    """ check if opt_exclude arguments not in args """

    for option_name in chk_args:
        if 'opt_exclude' not in chk_args[option_name]\
        or option_name not in args:
            continue

        for exclude_option in chk_args[option_name]['opt_exclude']:
            if exclude_option in args:
                log.error('opt [%s]: exclude option! ( %s )',
                          option_name,
                          exclude_option)
                return False

    return True


def opt_set_var(args, chk_args):
    """ set variables for option """

    dict_vars = {}
    for option_name in args:
        if option_name not in chk_args:
            continue

        set_var = chk_args[option_name].get('set_var', None)
        if set_var:
            for var_name in set_var:
                if set_var[var_name] == '@SELF':
                    set_var[var_name] = args[option_name]

            dict_vars.update(set_var)

    return dict_vars


def arg_type(option_name, option_value, chk_args):
    """ check if argument is from specified type """

    arg_type_list = chk_args[option_name].get('arg_type', None)
    if not arg_type_list:
        return True

    if not isinstance(option_value, tuple(arg_type_list)):
        log.error('opt, [%s]: argument has wrong type! ( %s != %s )',
                  option_name,
                  str(type(option_value))[8:-2],
                  [str(x)[8:-2] for x in arg_type_list])
        return False

    return True


def arg_char_min_max(option_name, option_value, chk_args):
    """ check if arg has min or max character """

    log_msg = {'to_low': 'arg, [%s]: has to less characters! ( %s < %s )',
               'to_high': 'arg, [%s]: has to much characters! ( %s > %s )'}

    char_min = chk_args[option_name].get('char_min', None)
    char_max = chk_args[option_name].get('char_max', None)
    log_args = [option_name, option_value]

    if char_min and char_min > len(option_value):
        log_args.append(char_min)
        log.error(log_msg['to_low'], tuple(log_args))
        return False

    if char_max and char_max < len(option_value):
        log_args.append(char_max)
        log.error(log_msg['to_high'], tuple(log_args))
        return False

    return True


def arg_int_min_max(option_name, option_value, chk_args):
    """ check if arg has min or max integer value """

    log_msg = {'to_low': 'arg, [%s]: int value is to low! ( %s < %s )',
               'to_high': 'arg, [%s]: int value is to high! ( %s > %s )'}

    int_min = chk_args[option_name].get('int_min', None)
    int_max = chk_args[option_name].get('int_max', None)
    log_args = [option_name, option_value]

    if int_min and int_min > option_value:
        log_args.append(int_min)
        log.error(log_msg['to_high'], tuple(log_args))
        return False

    if int_max and int_max < option_value:
        log_args.append(int_max)
        log.error(log_msg['to_high'], tuple(log_args))
        return False

    return True


def arg_float_min_max(option_name, option_value, chk_args):
    """ check if arg has min or max float value """

    log_msg = {'to_low': 'arg, [%s]: float value is to low! ( %s < %s )',
               'to_high': 'arg, [%s]: float value is to high! ( %s > %s )'}

    float_min = chk_args[option_name].get('float_min', None)
    float_max = chk_args[option_name].get('float_max', None)
    log_args = [option_name, option_value]

    if float_min and float_min > option_value:
        log_args.append(float_min)
        log.error(log_msg['to_low'], tuple(log_args))
        return False

    if float_max and float_max < option_value:
        log_args.append(float_max)
        log.error(log_msg['to_high'], tuple(log_args))
        return False

    return True


def arg_decp_min_max(option_name, option_value, chk_args):
    """ check if arg value has min or max decimal places """

    log_msg = {'to_low': 'arg, [%s]: float value has not enough decimal places!'
                         '( %s < %s )',
               'to_high': 'arg, [%s]: float value have to many decimal places!'
                          '( %s > %s )'}

    decp_min = chk_args[option_name].get('decp_min', None)
    decp_max = chk_args[option_name].get('decp_max', None)
    log_args = [option_name, option_value]

    if decp_min or decp_max:
        decp_value = len(str(option_value).split('.')[1])

    if decp_min and decp_min > decp_value:
        log_args.append(decp_min)
        log.error(log_msg['to_low'], tuple(log_args))
        return False

    if decp_max and decp_max < decp_value:
        log_args.append(decp_max)
        log.error(log_msg['to_high'], tuple(log_args))
        return False

    return True


def arg_list_min_max(option_name, option_value, chk_args):
    """ check if list has min or max elements """

    log_msg = {'to_low': 'arg, [%s]: list has not enough entries! ( %s < %s )',
               'to_high': 'arg, [%s]: list has to many entries! ( %s > %s )'}

    list_min = chk_args[option_name].get('list_min', None)
    list_max = chk_args[option_name].get('list_max', None)
    log_args = [option_name, option_value]

    if list_min and list_min > len(option_value):
        log_args.append(list_min)
        log.error(log_msg['to_low'], tuple(log_args))
        return False

    if list_max and list_max < len(option_value):
        log_args.append(list_max)
        log.error(log_msg['to_high'], tuple(log_args))
        return False

    return True


def arg_etype(option_name, option_value, chk_args):
    """ check if elements in a list are from specific types """

    check_element_types = chk_args[option_name].get('arg_etype', None)

    if check_element_types is None:
        return True

    for count, element in enumerate(option_value):
        if not isinstance(element, tuple(check_element_types)):
            log.error('arg, [%s]: element %s is from unexpectet type! '
                      '( %s != %s )',
                      option_name,
                      count,
                      str(type(element)).split("'")[1],
                      [str(x).split("'")[1] for x in check_element_types])
            return False

    return True


def arg_allow(option_name, option_value, chk_args):
    """ check if arg value is allowed """

    args_allow = chk_args[option_name].get('arg_allow', None)

    if args_allow is None:
        return True

    if option_value not in args_allow:
        log.error('arg, [%s]: argument is not allowed! ( %s != %s )',
                  option_name,
                  option_value,
                  args_allow)
        return False

    return True


def arg_deny(option_name, option_value, chk_args):
    """ check if arg value is denied """

    if 'arg_deny' in chk_args[option_name]:
        args_deny = chk_args[option_name]['arg_deny']
        if option_value in args_deny:
            log.error('arg, [%s]: argument is denied! ( %s = %s )',
                      option_name,
                      option_value,
                      args_deny)
            return False

    return True


def arg_check(option_name, option_value, chk_args):
    """ check arg value with specific function """

    if 'arg_check' not in chk_args[option_name]:
        return True

    if isinstance(chk_args[option_name]['arg_check'], list):
        list_check = chk_args[option_name]['arg_check']

    else:
        list_check = [chk_args[option_name]['arg_check']]

    for check in list_check:
        if check(option_value):
            log.debug('arg, [%s]: check success! ( %s -> %s )',
                      option_name,
                      str(check).split(' ')[1],
                      option_value)
        else:
            log.error('arg, [%s]: check error! ( %s -> %s )',
                      option_name,
                      str(check).split(' ')[1],
                      option_value)
            return False

    return True


def arg_default(args, chk_args):
    """ set default value for arg """

    for option_name in chk_args:
        if option_name in args:
            continue

        if 'arg_default' in chk_args[option_name]:
            default_value = chk_args[option_name]['arg_default']

            log.debug('arg, [%s]: setting default value! ( %s )',
                      option_name,
                      default_value)
            args[option_name] = default_value

    return args
