from Code_for_test.Grid_Challenge import gridChallenge
import unittest

class TestGridChallenge(unittest.TestCase):
    
    def test_grid_challenge_empty_grid(self):
        #  grid เป็น empty
        grid = []
        self.assertEqual(gridChallenge(grid), 'YES')

    def test_grid_challenge_single_row(self):
        # มีแถวเพียงหนึ่งแถว
        grid = ['xbcdezg']
        self.assertEqual(gridChallenge(grid), 'YES')

    def test_grid_challenge_single_character(self):
        # มีแต่ตัวอักษรเดียว
        grid = ['a', 'a', 'a', 'a', 'a']
        self.assertEqual(gridChallenge(grid), 'YES')

    def test_grid_challenge_yes(self):
        # มีคำตอบเป็น YES
        grid1 = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        grid2 = ['zzzzzwz','zzzzzzw','wzzzzzz','zzwzzzz','zzyzzzz','zzzzyzz','zzzzzyz']
        self.assertEqual(gridChallenge(grid1), 'YES')
        self.assertEqual(gridChallenge(grid2), 'YES')
        
    def test_grid_challenge_no(self):
        # มีคำตอบเป็น NO
        grid1 = ['ebacd', 'fghzj', 'olmkn', 'trpqs', 'xywuq'] 
        grid2 = ['vbznfwg','eacklwk','bmarzvp','rwgnjqd','xqddtln','wuxtduk','rzmfcik'] 
        self.assertEqual(gridChallenge(grid1), 'NO')
        self.assertEqual(gridChallenge(grid2), 'NO')

    def test_grid_challenge_single_column(self):
        # มีคอลัมน์เพียงหนึ่งคอลัมน์
        grid1 = ['a', 'b', 'c', 'd', 'e']
        grid2 = ['a', 'b', 'm', 'd', 'e']
        self.assertEqual(gridChallenge(grid1), 'YES')
        self.assertEqual(gridChallenge(grid2), 'NO')

    def test_grid_challenge_lowercase(self):
        # ตัวอักษรเป็น lowercase ทั้งหมด
        grid = ['edcba', 'jihgf', 'nmlko', 'sqprt', 'vuxyw']
        self.assertEqual(gridChallenge(grid), 'YES')

    def test_grid_challenge_uppercase(self):
        # ตัวอักษรเป็น uppercase ทั้งหมด
        grid = ['EDCBA', 'JIHGF', 'NMLKO', 'SQPRT', 'VUXYW']
        self.assertEqual(gridChallenge(grid), 'YES')

    def test_grid_challenge_mixed_case(self):
        # ตัวอักษรเป็น uppercase และ lowercase ผสมกัน
        grid = ['eDcBA', 'jIhGF', 'nMLko', 'sqprt', 'vUxYw']
        self.assertEqual(gridChallenge(grid), 'NO')
