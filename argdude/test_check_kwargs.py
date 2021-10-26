from .check_kwargs import *

def test_kw_unknown_true():
    kw_args = {'foo': 'bar'}
    kw_rules = {'foo': {}}
    r = kw_unknown(kw_args, kw_rules)
    assert r == True

def test_kw_unknown_false():
    kw_args = {'foo': 'bar'}
    kw_rules = {}
    r = kw_unknown(kw_args, kw_rules)
    assert r == False

def test_kw_ignore_true():
    kw_args = {'kw_ignore': ['foo']}
    kw_rules = {'foo': {}}
    r = kw_ignore(kw_args, kw_rules)
    assert kw_rules == {}

def test_kw_required_true():
    kw_args = {'foo': 'bar'}
    kw_rules = {'foo': {'kw_required': True}}
    r = kw_required(kw_args, kw_rules)
    assert r == True

def test_kw_required_false():
    kw_args = {}
    kw_rules = {'foo': {'kw_required': True}}
    r = kw_required(kw_args, kw_rules)
    assert r == False

def test_kw_include_true():
    kw_args = {'foo': 1, 'bar': 2}
    kw_rules = {'foo': {'kw_include': ['bar']}}
    assert kw_include(kw_args, kw_rules) == True

def test_kw_include_false():
    kw_args = {'foo': 1}
    kw_rules = {'foo': {'kw_include': ['bar']}}
    assert kw_include(kw_args, kw_rules) == False
  
def test_kw_exclude_true():
    kw_args = {'foo': 1}
    kw_rules = {'foo': {'kw_exclude': ['bar']}}
    assert kw_exclude(kw_args, kw_rules) == True

def test_kw_include_false():
    kw_args = {'foo': 1, 'bar': 2}
    kw_rules = {'foo': {'kw_include': ['bar']}}
    assert kw_include(kw_args, kw_rules) == True

def test_kwarg_default():
    kw_args = {}
    kw_rules = {'foo': {'arg_default': 'bar'}}
    assert kwarg_default(kw_args, kw_rules) == {'foo': 'bar'}

def test_kwarg_type_true():
    kw_rules = {'foo': {'arg_type': [str]}}
    assert kwarg_type('foo', 'bar', kw_rules) == True

def test_kwarg_type_false():
    kw_rules = {'foo': {'arg_type': [int]}}
    assert kwarg_type('foo', 'bar', kw_rules) == False

def test_kwarg_check_true():
    def chk_foo(x):
        return x['kw_value'] == 'bar'
    kw_rules = {'foo': {'arg_check': [chk_foo]}}
    assert kwarg_check('foo', 'bar', kw_rules) == True
      
def test_kwarg_check_false():
    def chk_foo(x):
        return x['kw_value'] == 'bar'
    kw_rules = {'foo': {'arg_check': [chk_foo]}}
    assert kwarg_check('foo', 'barf', kw_rules) == False

def test_check_kwargs():
    assert check_kwargs({}, {}) == {}

