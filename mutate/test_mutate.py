import unittest

from mutate.mutate import Mutations


class TestMutate(unittest.TestCase):
    MUTATING_WORD = "mutation"
    RIGHT_WORDS = frozenset((MUTATING_WORD, "mutatiop", "station"))
    WRONG_WORDS = frozenset(("sensation", "abbreviation", "ation"))

    def test_mutate_success(self):
        mutations = Mutations(self.MUTATING_WORD)
        self.assertEqual(436, len(mutations))
        self.assertTrue(self.RIGHT_WORDS.issubset(mutations))

    def test_mutate_failure(self):
        mutations = Mutations(self.MUTATING_WORD)
        self.assertEqual(436, len(mutations))
        self.assertTrue(not self.WRONG_WORDS.issubset(mutations))


if __name__ == '__main__':
    unittest.main()
