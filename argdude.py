import logging as log
log.getLogger().addHandler(log.NullHandler())



def init_chk_args(chk_args):
    """ initialyze chk_args """

    def stupid():
        return None

    keys = {'opt_required'      : [bool, type],
            'opt_required_bool' : [bool, type],
            'opt_include'       : [list],
            'opt_exclude'       : [list],
            'opt_set_var'       : [dict],
            'arg_type'          : [list],
            'char_min'          : [int],
            'char_max'          : [int],
            'int_min'           : [int],
            'int_max'           : [int],
            'float_min'         : [float],
            'float_max'         : [float],
            'decp_min'          : [int],
            'decp_max'          : [int],
            'list_min'          : [int],
            'list_max'          : [int],
            'arg_allow'         : [list],
            'arg_deny'          : [list],
            'arg_check'         : [type(stupid), list],
            'arg_default'       : [type(stupid), 
                                   str, int, float, list, dict, tuple],
            'set_var'           : [dict],
            'sys_arg'           : [list]}

    for option_name in chk_args:
        for chk_args_keyword in chk_args[option_name]:
            if chk_args_keyword not in keys:
                log.error('chk_args: keyword does not exist! ( %s )'
                          % chk_args_keyword)
                return False

            if type(chk_args[option_name][chk_args_keyword])\
                    not in keys[chk_args_keyword]:
                log.error('chk_args, [%s]: key value has wrong type! '
                          '( %s != %s )'
                          % (chk_args_keyword,
                             type(chk_args[option_name][chk_args_keyword]),
                             keys[chk_args_keyword]))
                return False

    return True



def check_args(args, chk_args):
    """ check args by chk_args definition """

    import lib_checkargs

    # init chk_args
    if not init_chk_args(chk_args):
        return False
    
    # set option variables
    chk_args['set_var'] = lib_checkargs.opt_set_var(args, chk_args)

    # set default arguments
    args.update(lib_checkargs.arg_default(args, chk_args))

    # check options
    for check_opt in [lib_checkargs.opt_unknown,
                      lib_checkargs.opt_ignore,
                      lib_checkargs.opt_required,
                      lib_checkargs.opt_required_bool,
                      lib_checkargs.opt_include,
                      lib_checkargs.opt_exclude]:
        if not check_opt(args, chk_args):
            return False

    # check arguments
    for option_name in args:
        option_value = args[option_name]

        for check_arg in [lib_checkargs.arg_type,
                          lib_checkargs.arg_allow,
                          lib_checkargs.arg_deny,
                          lib_checkargs.arg_char_min_max,
                          lib_checkargs.arg_int_min_max,
                          lib_checkargs.arg_float_min_max,
                          lib_checkargs.arg_decp_min_max,
                          lib_checkargs.arg_list_min_max,
                          lib_checkargs.arg_check]:
            if not check_arg(option_name, option_value, chk_args):
                return False

    return args

