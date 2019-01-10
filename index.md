# Argdude documentation


## Description


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
check for required options

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

### int_max

### float_min

### float_max

### decp_min

### decp_max

### arg_check


## Tests
```
import logging
from argdude_test import main

logging.basicConfig(format='%(asctime)s %(module)s %(funcName)s %(message)s', 
                    datefmt='%Y.%m.%d %H:%M:%S', 
                    level=logging.DEBUG)

main()
2019.01.10 11:55:26 lib_checkargs opt_unknown opt: unknown option! ( bar )
2019.01.10 11:55:26 lib_checkargs opt_required opt: is required but undefined! ( foo )
2019.01.10 11:55:26 lib_checkargs opt_required_bool opt: except one option but none is defined! ( ['foo', 'bar'] )
2019.01.10 11:55:26 lib_checkargs opt_include opt, [foo]: depends on option! ( bar )
2019.01.10 11:55:26 lib_checkargs opt_unknown opt: unknown option! ( bar )
2019.01.10 11:55:26 lib_checkargs arg_default arg, [foo]: setting default value! ( foo )
2019.01.10 11:55:26 lib_checkargs arg_type opt, [foo]: argument has wrong type! ( int != str )
2019.01.10 11:55:26 lib_checkargs arg_allow arg, [foo]: argument is not allowed! ( foo != ['bar'] )
2019.01.10 11:55:26 lib_checkargs arg_deny arg, [foo]: argument is denied! ( foo = ['foo'] )
2019.01.10 11:55:26 lib_checkargs arg_check arg, [foo]: check success! ( file_true -> argdude_test.py )
2019.01.10 11:55:26 lib_checkargs arg_check arg, [foo]: check error! ( file_true -> test_arskdfmsdkfm.py )
2019.01.10 11:55:26 lib_checkargs arg_char_min_max arg, [foo]: has to less characters! ( 2 < 3 )
2019.01.10 11:55:26 lib_checkargs arg_char_min_max arg, [foo]: has to much characters! ( 4 > 3 )
2019.01.10 11:55:26 lib_checkargs arg_int_min_max arg, [foo]: int value is to low! ( 41 < 42 )
2019.01.10 11:55:26 lib_checkargs arg_int_min_max arg, [foo]: int value is to high! ( 43 > 42 )
2019.01.10 11:55:26 lib_checkargs arg_float_min_max arg, [foo]: float value is to low! ( 42.0 < 42.1 )
2019.01.10 11:55:26 lib_checkargs arg_float_min_max arg, [foo]: float value is to high! ( 42.2 > 42.1 )
2019.01.10 11:55:26 lib_checkargs arg_decp_min_max arg, [foo]: float value has not enough decimal places! ( 42.12 < 3 )
2019.01.10 11:55:26 lib_checkargs arg_decp_min_max arg, [foo]: float value have to many decimal places!( 42.1234 > 3 )
2019.01.10 11:55:26 lib_checkargs arg_list_min_max arg, [foo]: list has not enough entries! ( 2 < 3 )
2019.01.10 11:55:26 lib_checkargs arg_list_min_max arg, [foo]: list has to many entries! ( 4 > 3 )
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
[ True | True ] arg_float_min
[ True | True ] arg_float_max
[ True | True ] arg_decp_min
[ True | True ] arg_decp_max
[ True | True ] arg_list_min
[ True | True ] arg_list_max
```
