from Code_for_test.Funny_string import funnyString
import unittest

class TestFunnyString(unittest.TestCase):
    
    def test_funny_string_funny(self):
        # สตริงที่ให้เป็น funny
        self.assertEqual(funnyString('acxz'), 'Funny')
        self.assertEqual(funnyString('aceg'), 'Funny')

    def test_funny_string_not_funny(self):
        # สตริงที่ให้ไม่เป็น funny
        self.assertEqual(funnyString('bcxz'), 'Not Funny')
        self.assertEqual(funnyString('bdgk'), 'Not Funny')

    def test_funny_string_empty(self):
        # สตริงว่าง
        self.assertEqual(funnyString(''), 'Funny')
    
    def test_funny_string_single_character(self):
        # สตริงมีเพียงอักขระเดียว
        self.assertEqual(funnyString('a'), 'Funny')
        self.assertEqual(funnyString('z'), 'Funny')

    def test_funny_string_repeated_characters(self):
        # สตริงมีตัวอักษรที่ซ้ำกัน
        self.assertEqual(funnyString('zzzz'), 'Funny')
        self.assertEqual(funnyString('aaaaef'), 'Not Funny')
    
    def test_funny_string_whitespace(self):
        # สตริงมีช่องว่าง
        self.assertEqual(funnyString('a cxz'), 'Not Funny')
        self.assertEqual(funnyString('Z  Y X WVU'), 'Not Funny')
    
    def test_funny_string_uppercase_lowercase(self):
        # สตริงมีตัวอักษรพิมพ์ใหญ่และเล็กรวมกัน
        self.assertEqual(funnyString('AbCdEfGhIjKlMnOpQrStUvWxYz'), 'Funny')
        self.assertEqual(funnyString('ZYXWVUTSRQPONMLKJIHGFEDCBA'), 'Funny')
        self.assertEqual(funnyString('Zyrzxrxskrtlpwpmtpxvowrxrpxq'), 'Not Funny')
        self.assertEqual(funnyString('eklrywzvpxtvoptlrskmskszvwzsuzxrtvyzwruqvyxusqwupnurqmtltnltsmuyxqoksyurpwqpv'), 'Not Funny')

    def test_funny_string_symbols(self):
        # สตริงมีสัญลักษณ์พิเศษ
        self.assertEqual(funnyString('!@#$%^&*()_+'), 'Not Funny')
        self.assertEqual(funnyString('!a@b^&*(c)_'), 'Not Funny')
        self.assertEqual(funnyString('{}|:"<>?`-=[];\',./'), 'Not Funny')





