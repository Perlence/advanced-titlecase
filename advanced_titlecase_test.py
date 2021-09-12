import pytest

import advanced_titlecase as atc


@pytest.mark.parametrize('title, expected', [
    ('hello world', 'Hello World'),
    ("hello's world", "Hello's World"),
    ('iii', 'III'),
    ('Hiii', 'Hiii'),
])
def test_titlecase(title, expected):
    assert atc.titlecase(title) == expected


@pytest.mark.parametrize('title, expected', [
    ('hello of the world', 'Hello of the World'),
    ('hello, of the world', 'Hello, of the World'),
    ('hello,of the world', 'Hello,Of the World'),
    ('of hello world', 'Of Hello World'),
    ('hello (of the world)', 'Hello (Of the World)'),
    ('hello (the world of)', 'Hello (The World Of)'),
    ('hello of the (the world)', 'Hello of The (The World)'),
    ('hello the world iii', 'Hello the World III'),
    ('the end complete iv: the road and the damned', 'The End Complete IV: The Road and the Damned'),
    ('(hello) the world', '(Hello) The World'),
    ('hello - the world', 'Hello - The World'),
    ('hello of. the world', 'Hello Of. The World'),
    ('hello the.', 'Hello The.'),
    ('hello the', 'Hello The'),
    ('in memory of...', 'In Memory of...'),
    ('...and the great cold death of the earth', '...and the Great Cold Death of the Earth'),
    ('we, the gods', 'We, the Gods'),
    ('aSHES DIVIDE', 'aSHES DIVIDE'),
    ('our fortress is burning... iii - the grain', 'Our Fortress Is Burning... III - The Grain'),
    ('cold fortress / of stars', 'Cold Fortress / Of Stars'),
    ('breeze ~ in monochrome night', 'Breeze ~ In Monochrome Night'),
    ('mine is yours to drown in (ours is the new tribe)', 'Mine Is Yours to Drown In (Ours Is the New Tribe)'),
    ('plan! the panama? of course', 'Plan! The Panama? Of Course'),
    ('she said, "of course"', 'She Said, "Of Course"'),
    ('the end of "hello world"', 'The End of "Hello World"'),
    ('ultra-bombastic', 'Ultra-Bombastic'),
])
def test_advanced_titlecase(title, expected):
    assert atc.advanced_titlecase(title) == expected
