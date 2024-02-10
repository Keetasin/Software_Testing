from Code_for_test.Two_Characters import alternate
import unittest

class TestAlternate(unittest.TestCase):
    def test_empty_string(self):
        # สตริงว่าง
        self.assertEqual(alternate(""), 0)

    def test_single_character(self):
        # สตริงที่มีเพียงตัวอักษรเดียว
        self.assertEqual(alternate("a"), 0)

    def test_identical_characters(self):
        # สตริงที่มีตัวอักษรซ้ำกัน
        self.assertEqual(alternate("aaaa"), 0)

    def test_alternating_characters(self):
        # สตริงที่มีตัวอักษรสลับกัน
        self.assertEqual(alternate("abcabc"), 4)

    def test_no_alternating_characters(self):
        # สตริงที่ไม่มีตัวอักษรที่สลับกัน
        self.assertEqual(alternate("aaaabbbb"), 0)

    def test_special_characters(self):
        # สตริงที่มีตัวอักษรพิเศษ
        self.assertEqual(alternate("a@b#c$d"), 2)

    def test_alternate_longest_alternating_string(self):
        # ทดสอบสตริงที่มีความยาวที่สุดที่เป็นตัวอักษรสลับกัน
        self.assertEqual(alternate("beabeefeab"), 5)

 
    


    


