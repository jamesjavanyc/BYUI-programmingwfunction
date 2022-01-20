# -*- coding: utf-8 -*-
# @Time    : 2022/1/12 13:59
# @Author  : Junzhou Liu
# @FileName: test_sentenses.py.py
# @Software: PyCharm
from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(4):
        word = get_noun(1)
        assert word in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(4):
        quantity = random.randint(2, 11)
        word = get_noun(quantity)
        assert word in plural_nouns


def test_get_verb():
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(4):
        quantity = random.randint(2, 11)
        word = get_verb(quantity, 'future')
        assert word in future_verbs

    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        quantity = random.randint(2, 11)
        word = get_verb(quantity, 'past')
        assert word in past_verbs

    present_single = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        word = get_verb(1, 'present')
        assert word in present_single

    present_plural = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        quantity = random.randint(2, 11)
        word = get_verb(quantity, 'present')
        assert word in present_plural


def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    for _ in range(4):
        word = get_preposition()
        assert word in prepositions


# exceed requirements
def test_get_adjective():
    adjectives = ['cute', 'lovely', 'strong', 'small']
    for _ in range(4):
        word = get_adjective()
        assert word in adjectives


def test_get_prepositional_phrase():
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond",
                    "by", "despite", "except", "for", "off", "on", "onto", "out", "over", "past", "to", "under", "with",
                    "without"]
    single_determiners = ["a", "one", "the"]
    plural_determiners = ["two", "some", "many", "the"]
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    adjectives = ['cute', 'lovely', 'strong', 'small']
    for _ in range(4):
        phrase = get_prepositional_phrase(1)
        word = phrase.split(" ")
        assert word[0] in prepositions
        assert word[1] in single_determiners
        assert word[2] in adjectives
        assert word[3] in single_nouns
    for _ in range(4):
        phrase = get_prepositional_phrase(random.randint(2, 11))
        word = phrase.split(" ")
        assert word[0] in prepositions
        assert word[1] in plural_determiners
        assert word[2] in adjectives
        assert word[3] in plural_nouns


pytest.main(["-v", "--tb=line", "-rN", __file__])
