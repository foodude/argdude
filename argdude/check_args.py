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
    """ check for unknown keywords """

    for option_name in args:
        if option_name not in chk_args:
            if option_name == 'opt_ignore':
                continue

            log.error('opt: unknown option! ( %s )', option_name)
            return False

    return True


def opt_ignore(args, chk_args):
    """ check if a keyword should be ignored """

    if 'opt_ignore' not in args:
        return chk_args

    for option_name in args['opt_ignore']:
        if option_name in chk_args:
            log.debug('opt: ignore option! ( %s )', option_name)
            chk_args.pop(option_name)

    return chk_args


def opt_required(args, chk_args):
    """ check if all required keywords in args """

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
    check if one of required_bool keywords exist in args """

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
    """ check if opt_include keywords in args """

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
    """ check if opt_exclude keywords not in args """

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
    """ set variables for keyword """

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


def arg_type(kw_name, kw_value, chk_args):
    """ check type from keyword argument """

    arg_type_list = chk_args[kw_name].get('arg_type', None)
    if not arg_type_list:
        return True

    if not isinstance(kw_value, tuple(arg_type_list)):
        log.error('opt, [%s]: argument has wrong type! ( %s != %s )',
                  kw_name,
                  str(type(kw_value))[8:-2],
                  [str(x)[8:-2] for x in arg_type_list])
        return False

    return True


def arg_char_min_max(kw_name, kw_value, chk_args):
    """ check number of character """

    char_min = chk_args[kw_name].get('char_min', None)
    char_max = chk_args[kw_name].get('char_max', None)

    if char_min and char_min > len(kw_value):
        log.error('arg, [%s]: has to less characters! ( %s > %s )',
                  kw_name, char_min, kw_value)
        return False

    if char_max and char_max < len(kw_value):
        log.error('arg, [%s]: has to many characters! ( %s > %s )',
                  kw_name, char_max, kw_value)
        return False

    return True


def arg_int_min_max(kw_name, kw_value, chk_args):
    """ check int value """

    int_min = chk_args[kw_name].get('int_min', None)
    int_max = chk_args[kw_name].get('int_max', None)

    if int_min and int_min > kw_value:
        log.error('arg, [%s]: int value is to low! ( %s > %s )',
                  kw_name, int_min, kw_value)
        return False

    if int_max and int_max < kw_value:
        log.error('arg, [%s]: int value is to high! ( %s < %s )',
                  kw_name, int_max, kw_value)
        return False

    return True


def arg_float_min_max(kw_name, kw_value, chk_args):
    """ check float value """

    float_min = chk_args[kw_name].get('float_min', None)
    float_max = chk_args[kw_name].get('float_max', None)

    if float_min and float_min > kw_value:
        log.error('arg, [%s]: float value is to low! ( %s > %s )',
                  kw_name, float_min, kw_value)
        return False

    if float_max and float_max < kw_value:
        log.error('arg [%s]: float value is to high! %s < %s )',
                  kw_name, float_max, kw_value)
        return False

    return True


def arg_decp_min_max(kw_name, kw_value, chk_args):
    """ check number of decimal places from a float value """

    decp_min = chk_args[kw_name].get('decp_min', None)
    decp_max = chk_args[kw_name].get('decp_max', None)

    if decp_min or decp_max:
        decp_value = len(str(kw_value).split('.')[1])
    else:
        return True

    if decp_min and decp_min > decp_value:
        log.error('arg, [%s]: float value has not enough decimal places!'
                  '( %s < %s )',
                  kw_name, decp_min, kw_value)
        return False

    if decp_max and decp_max < decp_value:
        log.error('arg, [%s]: float value has to many decimal places!'
                  '( %s < %s )',
                  kw_name, decp_max, kw_value)
        return False

    return True


def arg_list_min_max(kw_name, kw_value, chk_args):
    """ check number of elements in a list """

    list_min = chk_args[kw_name].get('list_min', None)
    list_max = chk_args[kw_name].get('list_max', None)

    if list_min and list_min > len(kw_value):
        log.error('args, [%s]: list has not enough entries! ( %s > %s )',
                  kw_name, list_min, kw_value)
        return False

    if list_max and list_max < len(kw_value):
        log.error('arg, [%s]: list has to many entries! ( %s < %s )',
                  kw_name, list_max, kw_value)
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


def arg_allow(kw_name, kw_value, chk_args):
    """ check if keyword value is allowed """

    args_allow = chk_args[kw_name].get('arg_allow', None)

    if args_allow is None:
        return True

    if kw_value not in args_allow:
        log.error('arg, [%s]: argument is not allowed! ( %s != %s )',
                  kw_name,
                  kw_value,
                  args_allow)
        return False

    return True


def arg_deny(kw_name, kw_value, chk_args):
    """ check if keyword value is denied """

    if 'arg_deny' in chk_args[kw_name]:
        args_deny = chk_args[kw_name]['arg_deny']
        if kw_value in args_deny:
            log.error('arg, [%s]: argument is denied! ( %s = %s )',
                      kw_name,
                      kw_value,
                      args_deny)
            return False

    return True


def arg_check(kw_name, kw_value, chk_args):
    """ check keyword value with specific function """

    if 'arg_check' not in chk_args[kw_name]:
        return True

    if isinstance(chk_args[kw_name]['arg_check'], list):
        list_check = chk_args[kw_name]['arg_check']

    else:
        list_check = [chk_args[kw_name]['arg_check']]

    for check in list_check:
        if check(kw_value):
            log.debug('arg, [%s]: check success! ( %s -> %s )',
                      kw_name,
                      str(check).split(' ')[1],
                      kw_value)
        else:
            log.error('arg, [%s]: check error! ( %s -> %s )',
                      kw_name,
                      str(check).split(' ')[1],
                      kw_value)
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


def check_args(args, chk_args):
    """ check keywords and keyword arguments by chk_args definition """

    # init chk_args
    if not initialize(chk_args):
        return False

    # set default arguments
    args.update(arg_default(args, chk_args))

    # set option variables
    chk_args['set_var'] = opt_set_var(args, chk_args)

    # check options
    for check_opt in [opt_unknown,
                      opt_ignore,
                      opt_required,
                      opt_required_bool,
                      opt_include,
                      opt_exclude]:
        if not check_opt(args, chk_args):
            return False

    # check arguments
    for option_name in args:
        option_value = args[option_name]

        for check_arg in [arg_type,
                          arg_etype,
                          arg_allow,
                          arg_deny,
                          arg_char_min_max,
                          arg_int_min_max,
                          arg_float_min_max,
                          arg_decp_min_max,
                          arg_list_min_max,
                          arg_check]:
            if not check_arg(option_name, option_value, chk_args):
                return False

    return args
