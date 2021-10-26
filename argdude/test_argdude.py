from argdude import Argdude

ad = Argdude({'foo': 'bar'})

def test_ad_args():
    assert ad.kw_args == {'foo': 'bar'}

def test_ad_add_rule():
    ad.add_rule('foo', kw_required=True)
    assert ad.kw_rules == {'foo': {'kw_required': True}}

def test_ad_check_kwargs():
    ad = Argdude()
    assert ad.check_kwargs() == {}

