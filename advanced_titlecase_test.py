import advanced_titlecase as atc

expected_fmt = "expected '{}', got '{}'"

titlecase_tests = [
    ('hello world', 'Hello World'),
    ("hello's world", "Hello's World"),
    ('iii', 'III'),
    ('Hiii', 'Hiii'),
]

advanced_titlecase_tests = [
    ('hello of the world', 'Hello of the World'),
    ('hello, of the world', 'Hello, of the World'),
    ('hello,of the world', 'Hello,Of the World'),
    ('of hello world', 'Of Hello World'),
    ('hello (of the world)', 'Hello (Of the World)'),
    ('hello (the world of)', 'Hello (The World Of)'),
    ('hello of the (the world)', 'Hello of the (The World)'),
    ('hello the world iii', 'Hello the World III'),
    ('the end complete iv: the road and the damned',
     'The End Complete IV: The Road and the Damned'),
    ('(hello) the world', '(Hello) The World'),
    ('hello - the world', 'Hello - The World'),
    ('hello of. the world', 'Hello Of. The World'),
    ('hello the.', 'Hello The.'),
    ('in memory of...', 'In Memory of...'),
]


def test_titlecase():
    for a in assertions(atc.titlecase, titlecase_tests):
        yield a


def test_advanced_titlecase():
    for a in assertions(atc.advanced_titlecase, advanced_titlecase_tests):
        yield a


def assertions(func, tests):
    for in_, out in tests:
        result = func(in_)
        yield (assert_equal, result, out,
               expected_fmt.format(out, result))


def assert_equal(a, b, message=''):
    assert a == b, message
