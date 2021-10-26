import logging as log

log.getLogger().addHandler(log.NullHandler())


def kw_unknown(kw_args, kw_rules):
    """ 
    info:
        check for unknown keywords
    
    usage:
        kw_unknown(kw_args, kw_rules)

    return:
        True | False
    """

    for kw_name in kw_args:
        if kw_name not in kw_rules:
            if kw_name == 'kw_ignore':
                continue

            log.error(f'Unknown keyword: {kw_name}')
            log.error(f'Alowed keywords: {kw_rules.keys()}')
            return False

    return True


def kw_ignore(kw_args, kw_rules):
    """ 
    info:
        check if a keyword should be ignored 

    usage:
        kw_ignore(kw_args, kw_rules)

    return:
        True | False
    """

    if 'kw_ignore' not in kw_args:
        return True

    for kw_name in kw_args['kw_ignore']:
        if kw_name in kw_rules:
            log.info(f'keyword: {kw_name}, ignored!')
            kw_rules.pop(kw_name)

    return True


def kw_required(kw_args, kw_rules):
    """
    info:
        check if all required keywords in kw_args 

    usage:
        kw_required(kw_args, kw_rules)

    example:
        kw_required({}, {'foo': {'kw_required': True}})

    return:
        True | False
    """

    for kw_name in kw_rules:
        required = kw_rules[kw_name].get('kw_required', False)
        if required is False:
            continue

        if kw_name not in kw_args:
            log.error(f'keyword is required but undefined: {kw_name}')
            return False

    return True


def kw_include(kw_args, kw_rules):
    """
    info:
        check if a keyword includes other keywords and if they 
        are present

    usage:
        kw_include(kw_args, kw_rules)

    example:
        kw_include({'foo': 1}, {'foo':{'kw_include': ['bar']}})

    return:
        True | False
    """
    
    for kw_name in kw_rules:
        list_kw_include = kw_rules[kw_name].get('kw_include', [])

        for kw_include in list_kw_include:
            if kw_name in kw_args and kw_include not in kw_args:
                log.error(f'Keyword: {kw_name}, depends on the following '
                          f'keywords: {list_kw_include}')
                return False

    return True



def kw_exclude(kw_args, kw_rules):
    """
    info:
        Check if a keyword excludes other keywords and if they
        are present

    usage:
        kw_exclude(kw_args, kw_rules)

    example:
        kw_exclude({'foo': 1, 'bar': 1}, {'foo': {'kw_exclude': ['bar']}})

    return:
        True | False
    """

    for kw_name in kw_rules:
        if kw_name not in kw_args:
            continue

        list_kw_exclude = kw_rules[kw_name].get('kw_exclude', [])
        
        for kw_exclude in list_kw_exclude:
            if kw_exclude in kw_args:
                log.error(
                    f'Keyword: {kw_name}, could not be used together '
                    f'with the following keywords: {list_kw_exclude}')
                return False

    return True



def kwarg_default(kw_args, kw_rules):
    """
    info:
        Set default keyword arguments

    usage:
        kwarg_default(kw_args, kw_rules)

    example:
        kwarg_default({}, {'foo': 'bar'})

    return:
        kw_args 
    """

    for kw_name in kw_rules:
        if kw_name in kw_args:
            continue

        arg_default = kw_rules[kw_name].get('arg_default', '!NONE!')
        if arg_default == '!NONE!':
            continue

        log.info(f'Keyword: {kw_name}, set default argument: {arg_default}')
        kw_args[kw_name] = arg_default

    return kw_args


def kwarg_type(kw_name, kw_value, kw_rules):
    """
    info:
        Check keyword arument type

    usage:
        kwarg_type(kw_name, kw_value, kw_rules)

    example:
        kwarg_type('foo', 42, {'foo': {'arg_type': [str]}})

    return:
        True | False
    """

    type_list = kw_rules[kw_name].get('arg_type', None)
    if not type_list:
        return True

    if not isinstance(kw_value, tuple(type_list)):
        log.error('Keyword: %s, has wrong type: %s != %s',
            kw_name,
            str(type(kw_value))[8:-2],
            [str(x)[8:-2] for x in type_list])
        return False

    return True


def kwarg_check(kw_name, kw_value, kw_rules):
    """
    info:
        execute check functions in your pyhon namespace

    usage:
        kwarg_check(kw_name, kw_value, kw_rules)

    example:
        from argdude.checks.file import file_true
        kw_rules = {'file_name': {'kwarg_check: [file_true]}
        kwarg_check('file_name', '../file', kw_rules)

    return:
        True | False
    """
    for test_func in kw_rules[kw_name].get('arg_check', []):
        func_arg = {'kw_name': kw_name,
                    'kw_value': kw_value,
                    'kw_rules': kw_rules[kw_name]}
        if test_func(func_arg):
            log.info(f'Keyword: {kw_name}, check: {test_func.__name__} '
                     f'succeed: {kw_value}')

        else:
            log.error('Keyword: {kw_name}, check: {test_func.__name__} '
                      f'failed: {kw_value}')

            return False

    return True


def check_kwargs(kw_args, kw_rules):
    """
    info:
        perform all cheks between kw_args and kw_rules

    usage:
        check_kwargs(kw_args, kw_rules

    example:
        kw_args = {'foo': 42}
        kw_rules = {'foo': {'kwarg_type': [str]}}
        check_kwargs(kw_args, kw_rules)

    return:
        True | False
    """
    # Testing keywords
    for test_function in [kw_unknown,
                          kw_ignore,
                          kw_required,
                          kw_include,
                          kw_exclude]:
        if not test_function(kw_args, kw_rules):
            return False

    # Set default keyword arguments
    kw_args.update(kwarg_default(kw_args, kw_rules))

    # Testing keyword arguments
    for kw_name in kw_args:
        for test_function in [kwarg_type,
                              kwarg_check]:
            if not test_function(kw_name,
                                 kw_args[kw_name],
                                 kw_rules):
                return False

    return kw_args
