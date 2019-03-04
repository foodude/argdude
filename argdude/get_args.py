#!/usr/bin/python
from sys import argv
import logging as log
log.getLogger().addHandler(log.NullHandler())



def get_sys_args_definition(chk_args):
    dict_sys_args = {}
    for option_name in chk_args:
        if 'sys_args' in chk_args[option_name]:
            for sys_arg_name in chk_args[option_name]['sys_args']:
                dict_sys_args[sys_arg_name] = option_name

    return dict_sys_args

        

def get_args_from_sys_args(sys_args, dict_sys_args):
    args = {}
    option_name = ''

    for arg in sys_args:
        if arg in dict_sys_args:
            option_name = dict_sys_args[arg]

            if option_name in args:
                log.error('opt: duplicate use of option! ( %s )' % arg)
                return False

            args[option_name] = []
            continue

        if not option_name:
            log.error('opt: unknown option! ( %s )' % arg )
            return False

        args[option_name].append(arg)

    return args



def check_number_of_args(option_name, option_value, chk_args):
    args = chk_args[option_name].get('args', 1)
    if type(args) == list:
        args_min, args_max = args[0], args[1]
        
    else:
        args_min, args_max = args, args


    if type(args_min) is not int or type(args_max) is not int:
        log.error('chk_args, [%s][%s]: must be int '
                  'or list with two int elements! ( %s )'
                  % (option_name,
                     'args',
                      args))
        return False


    args_count = len(option_value)
    if args_count < args_min:
        log.error('opt [%s]: has not enought arguments! ( %s < %s )'
                  % (option_name,
                     args_count,
                     args_min))
        return False
    
    elif args_count > args_max:
        log.error('opt [%s]: has to many arguments! ( %s > %s )'
                  % (option_name,
                     args_count,
                     args_max))
        return False

    else:
        return True
    



def arg_set_type(option_name, option_value, chk_args):
    args = []
    set_type = chk_args[option_name].get('set_type', False)
    if set_type:
        for arg in option_value:
            try:
                args.append(set_type(arg))
            except:
                log.error('opt [%s]: could not set_type! ( %s -> %s )'
                          % (option_name,
                             str(type(arg)).split("'")[1],
                             str(set_type).split("'")[1]))
                return False
    else:
        return option_value

    return args

    

def get_args(chk_args, sys_args=argv[:1]):
    ## GET: get_sys_args
    dict_sys_args = get_sys_args_definition(chk_args)

    ## search depending arguments
    args = get_args_from_sys_args(sys_args, dict_sys_args)
    if not args:
        return False

    for option_name in args:
        option_value = args[option_name]

        ## CHK: option argument count
        if not check_number_of_args(option_name, option_value, chk_args):
            return False

        ## SET: argument type:
        args[option_name] = arg_set_type(option_name, option_value, chk_args)
        if not args[option_name]:
            return False

    return args

