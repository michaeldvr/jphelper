import unittest
import jphelper.tests.assets as assets
import jphelper


class TestJPHelper(unittest.TestCase):

    def test_is_kanji(self):
        self.assertTrue(jphelper.is_kanji('明日'))
        self.assertFalse(jphelper.is_kanji('あした'))

    def test_is_hiragana(self):
        self.assertTrue(jphelper.is_hiragana('こんにちは'))
        self.assertFalse(jphelper.is_hiragana('今日は'))

    def test_is_katakana(self):
        self.assertTrue(jphelper.is_katakana('プログラミング'))
        self.assertFalse(jphelper.is_katakana('プログラミング言語'))

    def test_is_kana(self):
        self.assertTrue(jphelper.is_kana('あおいシャツ'))
        self.assertFalse(jphelper.is_kana('青いシャツ'))

    def test_match_reading(self):
        for row in assets.match_reading_tests:
            self.assertEqual(jphelper.match_reading(row[0], row[1], space='#', post_space='@'), row[2])

    def test_kanaize(self):
        for row in assets.kanaize:
            self.assertEqual(jphelper.kanaize(row[0], row[1]), row[2])


if __name__ == '__main__':
    pass
