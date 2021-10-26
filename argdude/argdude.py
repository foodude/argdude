from .check_kwargs import check_kwargs


class Argdude:
    """
    info:
        check keywords and keyword arguments
        on various conditions

    kw_rules tags:
        kw_require <True|False>
            Define if the keyword is required or not

        kw_include <[arg1, arg2, ...]>
            Define keywords which must be include to
            the current keyword

        kw_exclude <[arg1, arg2, ...]>
            Define keywords which cant be used with
            the current keyword

        arg_default <*>
            Define standard argument for the
            current keyword

        arg_type <[str, int, float, list, dict, ...]>
            Define from which type the keyword argument
            has to be

        arg_check <[my_check_01, my_check_02, ...]>
            Define aditional checks to keyword argument

    example:
        ad = Argdude({'foo': 'bar'})
        ad.add_rule('foo', arg_type=[str])
        ad.check_kwargs()
    """

    def __init__(self, kw_args={}):
        self.kw_args = kw_args
        self.kw_rules = {}

    def add_rule(self, kw_name, **args):
        """ add kw rule """
        self.kw_rules[kw_name] = args

    def check_kwargs(self):
        """ check args wit hkw rules """
        return check_kwargs(self.kw_args, self.kw_rules)
