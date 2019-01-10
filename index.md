# Argdude documentation


## Description


## Options

### opt_unknown


### opt_ignore


### opt_required
check for required options

```
in [1] args = {}

in [2] chk_args = {'foo': {'opt_required': True}}

in [3] check_args(args, chk_args)
out[3] opt: is required but undefined! ( foo )
```


### opt_required_bool

```
in [1] chk_args = {'foo': {'opt_required': bool},
                   'bar': {'opt_required': bool}}

in [2] args = {}

in [3] check_args(args, chk_args)
out[3] opt: except one option but none is defined! ( ['foo', 'bar'] )

```


### opt_include

```
in [1] chk_args = {'foo': {'opt_include': ['bar']},
                   'bar': {}}

in [2] args = {'foo': 'bar'}

in [3] check_args(args, chk_args)
opt, [foo]: depends on option! ( [bar] )
out[3] False
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

### arg_allow

### arg_deny

### char_min

### char_max

### int_min

### int_max

### float_min

### float_max

### decp_min

### decp_max

### arg_check


