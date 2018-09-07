import logging
from collections import OrderedDict
from functools import wraps
from string import ascii_lowercase

logging.basicConfig(format='%(message)s', level=logging.DEBUG)


def _collect_mutations(decorated):
    """
    Execute the decorated function and collect the result of execution
    (mutations) to the result set.

    :param decorated: the function that is going to be decorated.
    :return: the set of mutations
    """

    @wraps(decorated)
    def wrapper(*args, **kwargs):
        mutations = set()
        for mutation in decorated(*args, **kwargs):
            mutations.add(mutation)
        return mutations

    return wrapper


class Mutations:
    """
    A class representing a set of mutations.
    """

    def __init__(self, word):
        self._mutations = set(word)
        for mutations in (get_mutations(word)
                          for get_mutations in (
                                  self.get_delete_mutations,
                                  self.get_insert_mutations,
                                  self.get_replace_mutations,
                                  self.get_swap_mutations)):
            self._mutations |= mutations
        self._mutations = sorted(self._mutations)
        self.letter_mapping = OrderedDict()
        for mutation in self._mutations:
            self.letter_mapping.setdefault(mutation[0], []).append(mutation)
        for letter, mutations in self.letter_mapping.items():
            logging.debug("{:^2}-> {}".format(letter, ", ".join(mutations)))

    def __iter__(self):
        return iter(self._mutations)

    def __len__(self):
        return len(self._mutations)

    def __str__(self):
        return "{}".format(self.letter_mapping)

    @staticmethod
    def do_mutation(word, letters=('',), shift=1):
        for letter in letters:
            for i in range(len(word)):
                yield word[:i] + letter + word[i + shift:]

    @_collect_mutations
    def get_delete_mutations(self, word):
        """
        Return a generator containing words mutated by deleting a letter.

        :param word: the word for mutating.
        :return: the generator containing words mutated by deleting a letter.
        """
        yield from self.do_mutation(word)

    @_collect_mutations
    def get_insert_mutations(self, word):
        """
        Return a generator containing words mutated by inserting a letter between
        other ones.

        :param word: the word for mutating.
        :return: the generator containing words mutated by inserting a letter
        between other ones.
        """
        for letter in ascii_lowercase:
            yield letter + word
            yield word + letter
        yield from self.do_mutation(word, ascii_lowercase)

    @_collect_mutations
    def get_replace_mutations(self, word):
        """
        Return a generator containing words mutated by replacing a letter with
        ascii lowercase ones.

        :param word: the word for mutating.
        :return: the generator containing words mutated by replacing a letter with
        ascii lowercase ones.
        """
        yield from self.do_mutation(word, ascii_lowercase)

    @_collect_mutations
    def get_swap_mutations(self, word):
        """
        Return a generator containing words mutated by swapping a letter with acsii
        lowercase one.

        :param word: the word for mutating.
        :return: the generator containing words mutated by swapping a letter with
        acsii lowercase one.
        """
        yield from self.do_mutation(word, ascii_lowercase, 2)
