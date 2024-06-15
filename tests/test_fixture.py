import pytest


@pytest.fixture
def coll():
    return ['One', True, 3, [1, 'hexlet', [0]], 'cat', {}, '', [], False]


def test_compact(coll):
    assert coll == ['One', True, 3, [1, 'hexlet', [0]], 'cat', {}, '', [], False]
