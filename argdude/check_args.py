import logging as log
log.getLogger().addHandler(log.NullHandler())



def check_args(args, chk_args):
    """ check args by chk_args definition """

    import argdude.lib_checkargs as lib_checkargs

    # init chk_args
    if not lib_checkargs.initialize(chk_args):
        return False
    
    # set default arguments
    args.update(lib_checkargs.arg_default(args, chk_args))

    # set option variables
    chk_args['set_var'] = lib_checkargs.opt_set_var(args, chk_args)

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
                          lib_checkargs.arg_etype,
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

