from Code_for_test.Caesar_Cipher import caesarCipher
import unittest

class TestCaesarCipher(unittest.TestCase):
    def test_shift_within_range(self):
        # สตริงที่มีการเลื่อนอักษรภายในช่วงจำนวนตัวอักษร(26)
        self.assertEqual(caesarCipher("abc", 1), "bcd")
        self.assertEqual(caesarCipher("xyz", 3), "abc")
        self.assertEqual(caesarCipher("ABC", 2), "CDE")
        self.assertEqual(caesarCipher("XYZ", 4), "BCD")

    def test_shift_greater_than_26(self):
        # สตริงที่มีการเลื่อนที่มากกว่า 26
        self.assertEqual(caesarCipher("abc", 30), "efg")
        self.assertEqual(caesarCipher("ABC", 30), "EFG")

    def test_negative_shift(self):
        # การเลื่อนที่เป็นเลขลบ
        self.assertEqual(caesarCipher("abc", -1), "zab")
        self.assertEqual(caesarCipher("ABC", -2), "YZA")

    def test_shift_zero(self):
        # การเลื่อนที่เป็นเลขศูนย์
        self.assertEqual(caesarCipher("abc", 0), "abc")
        self.assertEqual(caesarCipher("ABC", 0), "ABC")

    def test_shift_over_alphabets(self):
        # การเลื่อนหลายตำเเหน่งมากๆ
        self.assertEqual(caesarCipher("abc", 260), "abc")
        self.assertEqual(caesarCipher("ABC", 260), "ABC")

    def test_empty_string(self):
        # สตริงว่าง
        self.assertEqual(caesarCipher("", 3), "")

    def test_non_alphabetic_characters(self):
        # สตริงที่ไม่ใช่ตัวอักษร
        self.assertEqual(caesarCipher("123_.:;][]}{", 5), "123_.:;][]}{")
        self.assertEqual(caesarCipher("!@#/*-+%*<>?", 10), "!@#/*-+%*<>?")

    def test_mixed_case(self):
        # สตริงที่มีการผสมผสานระหว่างตัวอักษรพิมพ์เล็ก ตัวอักษรพิมพ์ใหญ่ ช่องว่าง เเละ สตริงที่ไม่ใช่ตัวอักษร
        self.assertEqual(caesarCipher("A__bC123", 3), "D__eF123")
        self.assertEqual(caesarCipher("X y1Z!@#", 5), "C d1E!@#")