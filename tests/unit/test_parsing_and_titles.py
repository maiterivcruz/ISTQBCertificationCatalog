from types import SimpleNamespace

import pytest

from questions.views import _full_title, _parse_question

pytestmark = pytest.mark.unit


def make_question(text, answer='', correct_option=''):
    return SimpleNamespace(id=1, text=text, answer=answer,
                           correct_option=correct_option)


@pytest.mark.parametrize('title, expected', [
    ('Foundation Level', 'Certified Tester Foundation Level'),
    ('Certified Tester Foundation Level', 'Certified Tester Foundation Level'),
])
def test_full_title_prefix(title, expected):
    assert _full_title(title) == expected


def test_parse_splits_stem_and_options():
    q = make_question('What is testing?\na) One\nb) Two\nc) Three\nd) Four')
    parsed = _parse_question(q)
    assert parsed['stem_before'] == 'What is testing?'
    assert [letter for letter, _ in parsed['options']] == ['a', 'b', 'c', 'd']
    assert parsed['options'][1][1] == 'Two'


def test_parse_extracts_table():
    text = ('Intro\n[[TABLE]]\nH1|H2\nv1|v2\n[[/TABLE]]\nAfter\n'
            'a) A\nb) B')
    parsed = _parse_question(make_question(text))
    assert parsed['table']['headers'] == ['H1', 'H2']
    assert parsed['table']['rows'] == [['v1', 'v2']]
    assert parsed['stem_before'] == 'Intro'
    assert parsed['stem_after'] == 'After'


@pytest.mark.parametrize('answer, points', [
    ('Correct answer is c. K2 2', 2),
    ('Correct answer is a. K3 3', 3),
    ('Correct answer is b.', 1),
    ('', 1),
])
def test_points_parsed_from_answer(answer, points):
    parsed = _parse_question(make_question('Q?\na) A\nb) B', answer=answer))
    assert parsed['points'] == points


@pytest.mark.parametrize('correct, multiple', [('a', False), ('a,e', True), ('', False)])
def test_multiple_flag_follows_correct_option(correct, multiple):
    parsed = _parse_question(make_question('Q?\na) A\nb) B', correct_option=correct))
    assert parsed['multiple'] is multiple
