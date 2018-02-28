from unittest import mock

import foo


@mock.patch('foo.bar', return_value=False)
def test_baz_should_fail_if_bar_fails(mock_foo_bar):
    foo.bar = foo.dec(foo.bar)
    success = foo.baz()
    assert not success
