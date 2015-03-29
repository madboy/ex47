from nose.tools import *
from ex47 import parser

def test_peek():
    word_list = [('stop', 'the'),
            ('verb', 'go')]
    result = parser.peek(word_list)
    assert_equal(result, 'stop')

def test_match():
    word_list = [('stop', 'the'),
            ('verb', 'go')]
    result = parser.match(word_list, 'stop')
    assert_equal(result, ('stop', 'the'))

def test_skip():
    word_list = [('stop', 'the'),
            ('stop', 'of'),
            ('noun', 'press')]
    result = parser.skip(word_list, 'stop')
    assert_equal(word_list, [('noun', 'press')])

def test_verbs():
    word_list = [('stop', 'the'),
            ('stop', 'of'),
            ('verb', 'go')]
    result = parser.parse_verb(word_list)
    assert_equal(result, ('verb', 'go'))

def test_verbs_error():
    word_list = [('noun', 'door')]
    assert_raises(parser.ParserError,
            parser.parse_verb,
            word_list)

def test_objects_direction():
    word_list = [('stop', 'of'),
            ('direction', 'south'),
            ('stop', 'the'),
            ('subejct', 'bear')]
    result = parser.parse_object(word_list)
    assert_equal(result, ('direction', 'south'))

def test_objects_noun():
    word_list = [('noun', 'door')]
    result = parser.parse_object(word_list)
    assert_equal(result, ('noun', 'door'))

def test_objects_error():
    word_list = [('verb', 'go')]
    assert_raises(parser.ParserError,
            parser.parse_object,
            word_list)

def test_subject_noun():
    word_list = [('noun', 'table')]
    result = parser.parse_subject(word_list)
    assert_equal(result, ('noun', 'table'))

def test_subject_player():
    word_list = [('verb', 'go')]
    result = parser.parse_subject(word_list)
    assert_equal(result, ('noun', 'player'))

def test_subject_error():
    word_list = [('direction', 'east')]
    assert_raises(parser.ParserError,
            parser.parse_subject,
            word_list)

def test_sentence_stops():
    word_list = [('verb', 'run'), ('stop', 'to'), ('stop', 'the'), ('noun', 'hills')]
    result = parser.parse_sentence(word_list)
    assert_equal(result.subject, 'player')
    assert_equal(result.verb, 'run')
    assert_equal(result.object, 'hills')

def test_sentence_no_stops():
    word_list = [('noun', 'bear'), ('verb', 'eat'), ('noun', 'honey')]
    result = parser.parse_sentence(word_list)
    assert_equal(result.subject, 'bear')
    assert_equal(result.verb, 'eat')
    assert_equal(result.object, 'honey')

def test_sentence_error():
    word_list = [('stop', 'the'), ('stop', 'to')]
    assert_raises(parser.ParserError,
            parser.parse_sentence,
            word_list)
