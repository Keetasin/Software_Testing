from Code_for_test.Alternating_Characters import alternatingCharacters
import unittest

class TestAlternatingCharacters(unittest.TestCase):
    def test_empty_string(self):
        # สตริงว่าง
        self.assertEqual(alternatingCharacters(""), 0)

    def test_single_character_string(self):
        # สตริงที่มีเพียงตัวอักษรเดียว
        self.assertEqual(alternatingCharacters("A"), 0)

    def test_all_repeated_characters(self):
        # สตริงทุกตัวอักษรเหมือนกัน
        self.assertEqual(alternatingCharacters("AAAAAA"), 5)

    def test_repeated_characters(self):
        # สตริงที่มีตัวอักษรเหมือนกันติดกันหลายชุด
        self.assertEqual(alternatingCharacters("AAABBBAABB"), 6)

    def test_no_repeated_characters(self):
        # สตริงไม่มีตัวอักษรที่เหมือนกันติดกัน
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)

    def test_mixed_characters(self):
        # สตริงที่มีตัวอักษรที่เหมือนกันติดกัน และไม่เหมือนกันติดกัน
        self.assertEqual(alternatingCharacters("ABABBABAABABABABAAABA"), 4)

