from argdude import check_args
from argdude.checks.file import file_true


def test(func_name, arg_true, arg_false, chk_args):
    def t(x):
        if x is False:
            return False

        elif type(x) is dict:
            return True

        else:
            # add log statement for unknown behavior
            return False

    return {func_name: {
        'test_true': [False, True][t(check_args(arg_true, chk_args))],
        'test_false': [True, False][t(check_args(arg_false, chk_args))]}}


def test_opt_unknown():
    arg_true = {'foo': 'bar'}
    arg_false = {'bar': 'foo'}
    chk_args = {'foo': {}}
    return test('opt_unknown', arg_true, arg_false, chk_args)


def test_opt_required():
    arg_true = {'foo': 'bar'}
    arg_false = {'bar': 'foo'}
    chk_args = {'foo': {'opt_required': True},
                'bar': {}}
    return test('opt_required', arg_true, arg_false, chk_args)


def test_opt_required_bool():
    arg_true = {'foo': 'bar'}
    arg_false = {}
    chk_args = {'foo': {'opt_required': bool},
                'bar': {'opt_required': bool}}
    return test('opt_required_bool', arg_true, arg_false, chk_args)


def test_opt_include():
    arg_true = {'foo': 'bar',
                'bar': 'foo'}
    arg_false = {'foo': 'bar'}
    chk_args = {'foo': {'opt_include': ['bar']},
                'bar': {}}
    return test('opt_include', arg_true, arg_false, chk_args)


def test_opt_exclude():
    arg_true = {'foo': 'bar'}
    arg_false = {'foo': 'bar',
                 'bar': 'foo'}
    chk_args = {'foo': {'opt_exclude': ['bar']}}
    return test('opt_exclude', arg_true, arg_false, chk_args)


def test_opt_set_var():
    arg_true = {'foo': 'bar'}
    arg_false = {}
    chk_args = {'foo': {'set_var': {'a': '@SELF'}}}

    check_args(arg_false, chk_args)
    test_false = chk_args == {'foo': {'set_var': {'a': '@SELF'}},
                              'set_var': {}}

    check_args(arg_true, chk_args)
    test_true = chk_args == {'foo': {'set_var': {'a': 'bar'}},
                             'set_var': {'a': 'bar'}}

    return {'opt_set_var': {'test_true': test_true,
                            'test_false': test_false}}


def test_arg_type():
    arg_true = {'foo': 'bar'}
    arg_false = {'foo': 42}
    chk_args = {'foo': {'arg_type': [str]}}
    return test('arg_type', arg_true, arg_false, chk_args)


def test_arg_etype():
    arg_true = {'foo': [1, 1.123]}
    arg_false = {'foo': [1, 'bar']}
    chk_args = {'foo': {'arg_etype': [int, float]}}
    return test('arg_etype', arg_true, arg_false, chk_args)


def test_arg_allow():
    arg_true = {'foo': 'bar'}
    arg_false = {'foo': 'foo'}
    chk_args = {'foo': {'arg_allow': ['bar']}}
    return test('arg_allow', arg_true, arg_false, chk_args)


def test_arg_deny():
    arg_true = {'foo': 'bar'}
    arg_false = {'foo': 'foo'}
    chk_args = {'foo': {'arg_deny': ['foo']}}
    return test('arg_deny', arg_true, arg_false, chk_args)


def test_arg_check():
    arg_true = {'foo': '/etc/passwd'}
    arg_false = {'foo': 'test_arskdfmsdkfm.py'}
    chk_args = {'foo': {'arg_check': file_true}}
    return test('arg_check', arg_true, arg_false, chk_args)


def test_arg_char_min():
    arg_true = {'foo': 'bar'}
    arg_false = {'foo': 'ba'}
    chk_args = {'foo': {'char_min': 3}}
    return test('arg_char_min', arg_true, arg_false, chk_args)


def test_arg_char_max():
    arg_true = {'foo': 'bar'}
    arg_false = {'foo': 'barf'}
    chk_args = {'foo': {'char_max': 3}}
    return test('arg_char_max', arg_true, arg_false, chk_args)


def test_arg_int_min():
    arg_true = {'foo': 42}
    arg_false = {'foo': 41}
    chk_args = {'foo': {'int_min': 42}}
    return test('arg_int_min', arg_true, arg_false, chk_args)


def test_arg_int_max():
    arg_true = {'foo': 42}
    arg_false = {'foo': 43}
    chk_args = {'foo': {'int_max': 42}}
    return test('arg_int_max', arg_true, arg_false, chk_args)


def test_arg_float_min():
    arg_true = {'foo': 42.1}
    arg_false = {'foo': 42.0}
    chk_args = {'foo': {'float_min': 42.1}}
    return test('arg_float_max', arg_true, arg_false, chk_args)


def test_arg_float_max():
    arg_true = {'foo': 42.1}
    arg_false = {'foo': 42.2}
    chk_args = {'foo': {'float_max': 42.1}}
    return test('arg_float_max', arg_true, arg_false, chk_args)


def test_arg_decp_min():
    arg_true = {'foo': 42.123}
    arg_false = {'foo': 42.12}
    chk_args = {'foo': {'decp_min': 3}}
    return test('arg_decp_min', arg_true, arg_false, chk_args)


def test_arg_decp_max():
    arg_true = {'foo': 42.123}
    arg_false = {'foo': 42.1234}
    chk_args = {'foo': {'decp_max': 3}}
    return test('arg_decp_max', arg_true, arg_false, chk_args)


def test_arg_list_min():
    arg_true = {'foo': [1, 2, 3]}
    arg_false = {'foo': [1, 2]}
    chk_args = {'foo': {'list_min': 3}}
    return test('arg_list_min', arg_true, arg_false, chk_args)


def test_arg_list_max():
    arg_true = {'foo': [1, 2, 3]}
    arg_false = {'foo': [1, 2, 3, 4]}
    chk_args = {'foo': {'list_max': 3}}
    return test('arg_list_max', arg_true, arg_false, chk_args)


def test_arg_default():
    arg_true = {}
    arg_false = {'foo': 'bar'}
    chk_args = {'foo': {'arg_default': 'foo'}}
    test_args = check_args(arg_true, chk_args)
    if 'foo' not in test_args:
        test_true = False
    elif test_args['foo'] == 'foo':
        test_true = True
    else:
        test_true = False

    test_args = check_args(arg_false, chk_args)
    if test_args['foo'] == 'bar':
        test_false = True
    else:
        test_false = False

    return {'arg_default': {'test_true': test_true,
                            'test_false': test_false}}


def test_check_args():
    """
    info:
        test check_args functionality

    """

    list_tests = [test_opt_unknown,
                  test_opt_required,
                  test_opt_required_bool,
                  test_opt_include,
                  test_opt_exclude,
                  test_opt_set_var,
                  test_arg_default,
                  test_arg_type,
                  test_arg_etype,
                  test_arg_allow,
                  test_arg_deny,
                  test_arg_check,
                  test_arg_char_min,
                  test_arg_char_max,
                  test_arg_int_min,
                  test_arg_int_max,
                  test_arg_float_min,
                  test_arg_float_max,
                  test_arg_decp_min,
                  test_arg_decp_max,
                  test_arg_list_min,
                  test_arg_list_max]

    # run all tests and store its output
    # to a dictionary
    foo = {}
    for Test in list_tests:
        foo.update(Test())

    # print info
    for output in foo:
        print('[ %s | %s ] %s'
              % (foo[output]['test_true'],
                 foo[output]['test_false'],
                 output))

    # return 
    for test in foo:
        if foo[test]['test_true'] is False:
            return False

        elif foo[test]['test_false'] is False:
            return False

    return True
