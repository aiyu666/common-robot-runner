from libs.sample import Module


def test_get_true_func():
    assert Module.get_true() is True


def test_get_false_func():
    assert Module.get_false() is False