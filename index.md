
Table of Contents
=================

   * [Argdude documentation](#argdude-documentation)
      * [Description](#description)
      * [Disclaimer](#disclaimer)
   * [Class Argdude](#class-argdude)
      * [Description](#description-1)
      * [kw_rules](#kw_rules)
         * [kw_ignore]](#kw-ignore)
         * [kw_required](#kw-required)
         * [kw_include(#kw-include)
         * [kw_exclude(#kw-exclude)
         * [arg_default](#arg-default)
         * [arg_type](#arg-type)
         * [arg_check(#arg-check)
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
Ignore checks on keywords





# Pytest

## tests

## testing
```
pytest -v

cd argdude/
pytest -v test_argdude.py
pytest -v test_check_kwargs.py
```
