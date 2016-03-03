from rexpression import regex

def test_positive_match():
    assert 'foo bar' ==~ regex('^foo')
    assert 'foo bar' ==~ regex('bar$')

def test_negative_match():
    assert 'foo bar' !=~ regex('^boo')
    assert 'foo bar' !=~ regex('foo$')

def test_positive_equal():
    assert 'foo bar' ==  regex('foo bar')

def test_negative_equal():
    assert 'foo bar' !=  regex('bar foo')
