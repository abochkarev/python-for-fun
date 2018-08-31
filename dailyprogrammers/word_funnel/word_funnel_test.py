import unittest

import word_funnel


class TestWordFuller(unittest.TestCase):

    def test_positive(self):
        words = \
            [("leave", "eave"), ("reset", "rest"), ("dragoon", "dragon"),
             ("boats", "bots")]
        self.assertTrue(all(word_funnel.word_funnel(*pair) for pair in words))

    def test_negative(self):
        words = [("eave", "leave"), ("sleet", "lets"), ("skiff", "ski")]
        self.assertFalse(
            any(word_funnel.word_funnel(*pair) for pair in words))


if __name__ == '__main__':
    unittest.main()
