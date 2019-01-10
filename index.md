# Argdude documentation

   * [Argdude documentation](#argdude-documentation)
      * [Description](#description)
      * [Options](#options)
         * [opt_unknown](#opt_unknown)
         * [opt_ignore](#opt_ignore)
         * [opt_required](#opt_required)
         * [opt_required_bool](#opt_required_bool)
         * [opt_include](#opt_include)
         * [opt_exclude](#opt_exclude)
      * [Arguments](#arguments)
         * [arg_type](#arg_type)
         * [arg_allow](#arg_allow)
         * [arg_deny](#arg_deny)
         * [char_min](#char_min)
         * [char_max](#char_max)
         * [int_min](#int_min)
         * [int_max](#int_max)
         * [float_min](#float_min)
         * [float_max](#float_max)
         * [decp_min](#decp_min)
         * [decp_max](#decp_max)
         * [arg_check](#arg_check)
      * [Tests](#tests)



## Description
Argdude is a library to test keyword arguments on various conditions


## Disclaimer 
I apologize for my short text versions and errors contained therein.
English is not my native language but i will try to fix all formal and 
linguistic errors in this repository

Please note that argdude is in a early stage and many changes
can happen 

I've tested argdude exclusively on Linux, but it should also run on other
operating systems.
The module 'argdude_checks', is Linux only but not necessary. The checks 
contained therein can be replaced by your own as decribed in point 'arg_check'



## Introduction
For all code examples below, the following is required
```
import logging
from argdude import check_args

logging.basicConfig(format='%(message)s', level=logging.DEBUG)
```
Of course, you can use any log format you prefer

To get a first overview you can look at the point 'Real world example'.


## Options

### opt_unknown
```
chk_args = {}

args = {'foo': 'bar'}

in [1] check_args(args, chk_args)
opt: unknown option! ( foo )
out[1] False
```


### opt_ignore
```
chk_args = {'foo': {'opt_required': True}

args = {'opt_ignore': ['foo']}

in [1] check_args(args, chk_args)
opt: ignore option! ( foo )
out[1] {}
```


### opt_required
```
args = {}

chk_args = {'foo': {'opt_required': True}}

in [1] check_args(args, chk_args)
out[1] opt: is required but undefined! ( foo )
```


### opt_required_bool

```
chk_args = {'foo': {'opt_required': bool},
            'bar': {'opt_required': bool}}

args = {}

in [1] check_args(args, chk_args)
opt: except one option but none is defined! ( ['foo', 'bar'] )
out[1] False

```


### opt_include

```
chk_args = {'foo': {'opt_include': ['bar']},
            'bar': {}}

args = {'foo': 'bar'}

in [1] check_args(args, chk_args)
opt, [foo]: depends on option! ( [bar] )
out[1] False
```


### opt_exclude
```
chk_args = {'foo': {'opt_exclude': ['bar']},
            'bar': {}}

args = {'foo': 'bar', 'bar': 'foo'}

in [1] check_args(args, chk_args)
opt [foo]: could not be used with option! ( [bar] )
out[1] False
```


## Arguments

### arg_type
```
chk_args = {'foo': {'arg_type': int}

args = {'foo': 'fourty-two'}

in [1] check_args(args, chk_args)
opt, [foo]: argument has wrong type! ( str != int )
out[1] False
```

### arg_allow
```
chk_args = {'foo': {'arg_allow': ['bar']}}

args = {'foo': 'foobar'}

in [1] check_args(args, chk_args)
arg, [foo]: argument is not allowed! ( foobar != ['bar'] )
out[1] False
```

### arg_deny
```
chk_args = {'foo': {'arg_deny': ['bar']}}

args = {'foo': 'bar'}

in [1] check_args(args, chk_args)
arg, [foo]: argument is denied! ( bar = ['bar'] )
out[1] False
```

### char_min
```
chk_args = {'foo': {'char_min': 4}}

args = {'foo': 'bar'}

in [1] check_args(args, chk_args)
arg, [foo]: has to less characters! ( 3 < 4 )
out[1] False
```

### char_max
```
chk_args = {'foo': {'char_max': 2}}

args = {'foo': 'bar'}

in [1] check_args(args, chk_args)
arg, [foo]: has to much characters! ( 3 > 2 )
out[1] False
```

### int_min
```
chk_args = {'foo': {'int_min': 1}}

args = {'foo': 0}

in [1] check_args(args, chk_args)
arg, [foo]: int value is to low! ( 0 < 1 )
out[1] False
```

### int_max
```
chk_args = {'foo': {'int_max': 1}}

args = {'foo': 0}

in [1] check_args(args, chk_args)
arg, [foo]: int value is to high! ( 2 > 1 )
out[1] False
```


### float_min
```
chk_args = {'foo': {'float_min': 0.2}}

args = {'foo': 0.1}

in [1] check_args(args, chk_args)
arg, [foo]: float value is to low! ( 0.1 < 0.2 )
out[1] False
```


### float_max
```
chk_args = {'foo': {'float_max': 0.1}}

args = {'foo': 0}

in [1] check_args(args, chk_args)
arg, [foo]: float value is to high! ( 0.2 > 0.1 )
out[1] False
```


### decp_min
```
chk_args = {'foo': {'decp_min': 3}}

args = {'foo': 0.12}

in [1] check_args(args, chk_args)
arg, [foo]: float value has not enough decimal places! ( 0.12 < 3 )
out[1] False
```


### decp_max
```
chk_args = {'foo': {'int_max': 3}}

args = {'foo': 0.1234}

in [1] check_args(args, chk_args)
arg, [foo]: float value have to many decimal places!( 0.1234 > 3 )
out[1] False
```


### arg_check
```
from argdude_check in user_name_true

chk_args = {'user_name': {'arg_check': [user_name_false]}}

in [1] args = {'user_name': 'aquaman'}
arg, [foo]: check error! ( user_name_true -> aquaman )
out[1] False

in [2] args = {'user_name': 'root'}
arg, [foo]: check success! ( user_name_true -> root )
out[2] {'user_name': 'root'}
```

write your own check
```
def the_answer(x):
    return x == 42

chk_args = {'answere': {'arg_check': [the_answer]}}

args = {'answer': 42}

in [1] check_args(args, chk_args)
arg, [foo]: check success! ( the_answer -> 42 )
out[1] {'answer': 42}
```


## Tests
```
import logging
from argdude_test import main

logging.basicConfig(level=logging.DEBUG)

main()
ERROR:root:opt: unknown option! ( bar )
ERROR:root:opt: is required but undefined! ( foo )
ERROR:root:opt: except one option but none is defined! ( ['foo', 'bar'] )
ERROR:root:opt, [foo]: depends on option! ( bar )
ERROR:root:opt: unknown option! ( bar )
DEBUG:root:arg, [foo]: setting default value! ( foo )
ERROR:root:opt, [foo]: argument has wrong type! ( int != str )
ERROR:root:arg, [foo]: argument is not allowed! ( foo != ['bar'] )
ERROR:root:arg, [foo]: argument is denied! ( foo = ['foo'] )
DEBUG:root:arg, [foo]: check success! ( file_true -> argdude_test.py )
ERROR:root:arg, [foo]: check error! ( file_true -> test_arskdfmsdkfm.py )
ERROR:root:arg, [foo]: has to less characters! ( 2 < 3 )
ERROR:root:arg, [foo]: has to much characters! ( 4 > 3 )
ERROR:root:arg, [foo]: int value is to low! ( 41 < 42 )
ERROR:root:arg, [foo]: int value is to high! ( 43 > 42 )
ERROR:root:arg, [foo]: float value is to low! ( 42.0 < 42.1 )
ERROR:root:arg, [foo]: float value is to high! ( 42.2 > 42.1 )
ERROR:root:arg, [foo]: float value has not enough decimal places! ( 42.12 < 3 )
ERROR:root:arg, [foo]: float value have to many decimal places!( 42.1234 > 3 )
ERROR:root:arg, [foo]: list has not enough entries! ( 2 < 3 )
ERROR:root:arg, [foo]: list has to many entries! ( 4 > 3 )
[ True | True ] opt_unknown
[ True | True ] opt_required
[ True | True ] opt_required_bool
[ True | True ] opt_include
[ True | True ] opt_exclude
[ True | True ] opt_set_var
[ True | True ] arg_default
[ True | True ] arg_type
[ True | True ] arg_allow
[ True | True ] arg_deny
[ True | True ] arg_check
[ True | True ] arg_char_min
[ True | True ] arg_char_max
[ True | True ] arg_int_min
[ True | True ] arg_int_max
[ True | True ] arg_float_max
[ True | True ] arg_decp_min
[ True | True ] arg_decp_max
[ True | True ] arg_list_min
[ True | True ] arg_list_max
```
