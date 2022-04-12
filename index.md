
Table of Contents
=================

   * [Argdude documentation](#argdude-documentation)
      * [Description](#description)
      * [Disclaimer](#disclaimer)
   * [Class Argdude](#class-argdude)
      * [Description](#description-1)
      * [kw_rules](#kw_rules)
         * [kw_ignore](#kw_ignore)
         * [kw_required](#kw-required)
         * [kw_include](#kw_include)
         * [kw_exclude](#kw_exclude)
         * [arg_default](#arg_default)
         * [arg_type](#arg_type)
         * [arg_check](#arg_check)
   * [Examples](#examples)
   * [Pytest](#tests)
      * [tests](#tests)
      * [testing](#testing)


# Argdude documentation

## Description
Argdude is a library to test keywords and keyword arguments on various conditions


## Disclaimer 
I apologize for my short text versions and errors contained therein.
English is not my native language but i will try to fix all formal and 
linguistic errors in this repository

Please note that argdude is in a early stage and many changes
can happen 

I've tested argdude exclusively on Linux, but it should also run on other
operating systems.
The modules in 'argdude.checks', are Linux only but not necessary. The checks 
contained therein are examples and can be replaced by your own as decribed in 
point 'arg_check'



# Class Argdude
## Description
This Class perform various checks on a dictionary like kwargs.
In the context of argdude it is called 'kw_args'
The checks which will be performed come from a dictionary,
which is called 'kw_rules'


## kw_rules
foo bar

### kw_ignore
Keywords which are not checked.

### kw_required
Keywords which are expected in kwargs.

### kw_include
Keywords which have to be present for a certain keyword.

### kw_exclude
Keywords which are not allowed to be present for a certain keyword.

### arg_default
Define default arguments for keywords.

### arg_type
Define the type / types for keyword arguments.

### arg_check
Perform check functions in your namespace for keyword arguments.


# Examples
Basic usage
```
import argdude

ad = argdude.Argdude()
ad.add_rule('file_name', arg_default='/etc/passwd', arg_type=[str]
ad.check_kwargs()
```

Advanced example
```
import logging
import argdude
from argdude.checks.file import file_r_true
from argdude.checks.linux.user import user_name_true

kwargs = {'file_name': '/etc/passwd',
        'user_name': 'root'}
        
ad = argdude.Argdude(kwargs)
ad.add_rule('file_name', 
  kw_required=True,
  kw_include=['user_name']
  arg_type=[str]
  arg_check=[file_r_true])
ad.add_rule('user_name',
  arg_default='root',
  arg_type=[str],
  arg_check=[user_name_true])
ad.check_kwargs()
```

In a function
```
from argdude.checks.linux.user import user_name_true

def create_user(**kwargs):
  ad = argdude.Argdude(kwargs)
  ad.add_rule('user_name',
    kw_required=True,
    arg_default='root',
    arg_type=[str],
    arg_check=[user_name_true]
  args = ad.check_kwargs()
  if not args:
    return False
    
  ...
```

Write your owne check function
```
import logging
import argdude

def real_user(user_name):
  return user_name == 'spiderman'
  
ad = argdude.Argdude()
ad.kw_args = {'user_name': 'aquaman'}
ad.add_rule('user_name', arg_check=[real_user]
ad.check_kwargs()
```



# Pytest

## tests
test_argdude.py
test_check_kwargs.py

## testing
```
pytest -v

cd argdude/
pytest -v test_argdude.py
pytest -v test_check_kwargs.py
```
