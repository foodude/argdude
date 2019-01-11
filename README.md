# Argdude
Argdude is a Python library to test keyword arguments on various conditions

## Install
At the moment argdude is not packaged
```
cd /you/project
git clone https://github.com/foodude/argdude.git
```

## Usage
```
from argdude import check_args

def dummy(**args):
  chk_args = {}
  args = check_args(args, chk_args)
```

## Documentation
[Argdude documentation](https://foodude.github.io/argdude)

## License
[GPL v. 3](https://github.com/foodude/argdude/blob/master/LICENSE)
