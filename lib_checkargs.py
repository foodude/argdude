import logging as log
log.getLogger().addHandler(log.NullHandler())



def opt_unknown(args, chk_args):
    for option_name in args:
        if option_name not in chk_args:
            if option_name == 'opt_ignore':
                continue

            log.error('opt: unknown option! ( %s )' % option_name)
            return False

    return True



def opt_ignore(args, chk_args):
    if 'opt_ignore' not in args:
        return chk_args

    for option_name in args['opt_ignore']:
        if option_name in chk_args:
            log.debug('opt: ignore option! ( %s )' % option_name)
            chk_args.pop(option_name)

    return chk_args



def opt_required(args, chk_args):
    for option_name in chk_args:
        if 'opt_required' not in chk_args[option_name]:
            continue

        if chk_args[option_name]['opt_required'] is True:
            if option_name not in args:
                log.error('opt: is required but undefined! ( %s )'
                          % option_name)
                return False

    return True



def opt_required_bool(args, chk_args):
    required_bool = []
    for option_name in chk_args:
        if 'opt_required' not in chk_args[option_name]:
            continue

        if chk_args[option_name]['opt_required'] is bool:
            required_bool.append(option_name)

    for option_name in required_bool:
        if option_name in args:
            return True

    if required_bool:
        log.error('opt: except one option but none is defined! ( %s )'
                  % str(required_bool))
        return False

    return True



def opt_include(args, chk_args):
    for option_name in chk_args:
        if 'opt_include' not in chk_args[option_name]:
            continue

        for include_option in chk_args[option_name]['opt_include']:
            if include_option not in args:
                log.error('opt, [%s]: depends on option! ( %s )'
                          % (option_name,
                             include_option))
                return False

    return True



def opt_exclude(args, chk_args):
    for option_name in chk_args:
        if 'opt_exclude' not in chk_args[option_name]:
            continue

        for exclude_option in chk_args[option_name]['opt_exclude']:
            if exclude_option in args:
                log.error('opt [%s]: exclude option! ( %s )'
                          % (option_name,
                             exclude_option))
                return False

    return True



def opt_set_var(args, chk_args):
    dict_vars = {}
    for option_name in args:
        if not option_name in chk_args:
            continue

        set_var = chk_args[option_name].get('set_var', None)
        if set_var:
            for var_name in set_var:
                if set_var[var_name] == '@SELF':
                    set_var[var_name] = args[option_name]

            dict_vars.update(set_var)

    return dict_vars



def arg_type(option_name, option_value, chk_args):
    if 'arg_type' in chk_args[option_name]:
        option_type_list = chk_args[option_name]['arg_type']
    else:
        return True

    for option_type in option_type_list:
        if option_type is not type(option_value):
            log.error('opt, [%s]: argument has wrong type! ( %s != %s )'
                      % (option_name,
                         str(type(option_value))[8:-2],
                         str(option_type)[8:-2]))
            return False

    return True



def arg_char_min_max(option_name, option_value, chk_args):
    if 'char_min' in chk_args[option_name]:
        char_min = chk_args[option_name]['char_min']
        if len(option_value) < char_min:
            log.error('arg, [%s]: has to less characters! ( %s < %s )'
                      % (option_name,
                         len(option_value),
                         char_min))
            return False


    if 'char_max' in chk_args[option_name]:
        char_max = chk_args[option_name]['char_max']
        if len(option_value) > char_max:
            log.error('arg, [%s]: has to much characters! ( %s > %s )'
                      % (option_name,
                         len(option_value),
                         char_max))
            return False

    return True



def arg_int_min_max(option_name, option_value, chk_args):
    if 'int_min' in chk_args[option_name]:
        int_min = chk_args[option_name]['int_min']
        if option_value < int_min:
            log.error('arg, [%s]: int value is to low! ( %s < %s )'
                      % (option_name,
                         option_value,
                         int_min))
            return False


    if 'int_max' in chk_args[option_name]:
        int_max = chk_args[option_name]['int_max']
        if option_value > int_max:
            log.error('arg, [%s]: int value is to high! ( %s > %s )'
                      % (option_name,
                         option_value,
                         int_max))
            return False

    return True



def arg_float_min_max(option_name, option_value, chk_args):
    if 'float_min' in chk_args[option_name]:
        float_min = chk_args[option_name]['float_min']
        if option_value < float_min:
            log.error('arg, [%s]: float value is to low! ( %s < %s )'
                      % (option_name,
                         option_value,
                         float_min))
            return False


    if 'float_max' in chk_args[option_name]:
        float_max = chk_args[option_name]['float_max']
        if option_value > float_max:
            log.error('arg, [%s]: float value is to high! ( %s > %s )'
                      % (option_name,
                         option_value,
                         float_max))
            return False

    return True



def arg_decp_min_max(option_name, option_value, chk_args):
    if 'decp_min' in chk_args[option_name]:
        decp_min = chk_args[option_name]['decp_min']
        if len(str(option_value).split('.')[1]) < decp_min:
            log.error('arg, [%s]: float value has not enough decimal places! ' 
                      '( %s < %s )' % (option_name,
                                       option_value,
                                       decp_min))
            return False

    if 'decp_max' in chk_args[option_name]:
        decp_max = chk_args[option_name]['decp_max']
        if len(str(option_value).split('.')[1]) > decp_max:
            log.error('arg, [%s]: float value have to many decimal places!'
                      '( %s > %s )' % (option_name,
                                       option_value,
                                       decp_max))
            return False

    return True



def arg_list_min_max(option_name, option_value, chk_args):
    if 'list_min' in chk_args[option_name]:
        list_min = chk_args[option_name]['list_min']
        if len(option_value) < list_min:
            log.error('arg, [%s]: list has not enough entries! ( %s < %s )'
                      % (option_name,
                         len(option_value),
                         list_min))
            return False

    if 'list_max' in chk_args[option_name]:
        list_max = chk_args[option_name]['list_max']

        if len(option_value) > list_max:
            log.error('arg, [%s]: list has to many entries! ( %s > %s )'
                      % (option_name,
                         len(option_value),
                         list_max))
            return False

    return True



def arg_allow(option_name, option_value, chk_args):
    if 'arg_allow' in chk_args[option_name]:
        args_allow = chk_args[option_name]['arg_allow']
        if option_value not in args_allow:
            log.error('arg, [%s]: argument is not allowed! ( %s != %s )'
                      % (option_name,
                         option_value,
                         args_allow))
            return False

    return True



def arg_deny(option_name, option_value, chk_args):
    if 'arg_deny' in chk_args[option_name]:
        args_deny = chk_args[option_name]['arg_deny']
        if option_value in args_deny:
            log.error('arg, [%s]: argument is denied! ( %s = %s )'
                      % (option_name,
                         option_value,
                         args_deny))
            return False

    return True



def arg_check(option_name, option_value, chk_args):

    if 'arg_check' not in chk_args[option_name]:
        return True

    if type(chk_args[option_name]['arg_check']) == list:
        list_check = chk_args[option_name]['arg_check']
    else:
        list_check = [chk_args[option_name]['arg_check']]

    for check in list_check:
        if check(option_value):
            log.debug('arg, [%s]: check success! ( %s -> %s )'
                      % (option_name,
                         str(check).split(' ')[1],
                         option_value))
        else:
            log.error('arg, [%s]: check error! ( %s -> %s )'
                      % (option_name,
                         str(check).split(' ')[1],
                         option_value))
            return False

    return True



def arg_default(args, chk_args):
    for option_name in chk_args:
        if option_name in args:
            return args

        if 'arg_default' in chk_args[option_name]:
            default_value = chk_args[option_name]['arg_default']

            log.debug('arg, [%s]: setting default value! ( %s )'
                      % (option_name,
                         default_value))
            args[option_name] = default_value

    return args
