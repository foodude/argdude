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


