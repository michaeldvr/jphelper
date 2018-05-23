import unittest
import jphelper.number as number
import jphelper.tests.assets as assets


class TestNumber(unittest.TestCase):

    def test_japanize_kana(self):
        for row in assets.japanize_kana:
            self.assertEqual(number.to_japanese(row[0], row[1], row[2], row[3], row[4]), row[5])

    def test_japanize_kanji(self):
        for row in assets.japanize_kanji:
            self.assertEqual(number.to_japanese(row[0], row[1], row[2], row[3], row[4]), row[5])

    def test_japanize_minus(self):
        for row in assets.japanize_minus:
            self.assertEqual(number.to_japanese(row[0], row[1], row[2], row[3], row[4]), row[5])

    def test_japanize_decimals(self):
        for row in assets.japanize_decimals:
            self.assertEqual(number.to_japanese(row[0], row[1], row[2], row[3], row[4]), row[5])

    def test_group_unit(self):
        self.assertEqual(number.group_unit(123), '123')
        self.assertEqual(number.group_unit(-5320123232.32, separator='|', decimal_separator=':'), '-53|2012|3232:32')

    def test_kanji_grouping(self):
        self.assertEqual(number.kanji_grouping(-15124), '-1万5124')
        self.assertEqual(number.kanji_grouping(-2345678.90123, use_hiragana=True, use_minus_sign=False),
                         'マイナス234まん5678てん90123')

    def test_shorten(self):
        self.assertEqual(number.shorten(12345678987), '123.4億')


if __name__ == '__main__':
    pass