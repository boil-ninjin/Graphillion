import unittest
from pathlib import Path
import numpy as np
import sys
sys.path.append(str(Path(__file__).parent.parent))
sys.path.append(str(Path(__file__).parent.parent / "forLocal"))

import forLocal.ChangeCoord
from graphillion import GraphSet


class TestChanging(unittest.TestCase):
    def setUp(self):
        
        self.c = forLocal.ChangeCoord.ChangeCoordandSerial()       

    def test_onecase_inSerial(self):
        self.g = [(0, 1), (0, 2), (0, 3), (1, 8), (1, 9), (8, 15), (9, 16)] 
        self.cg = self.c.SerialtoCoord(self.g)
        self.scg = self.c.CoordtoSerial(self.cg)
        self.assertEqual(self.g, list(self.scg))

    def test_inSerial(self):
        self.a = np.loadtxt("tests/test.txt", dtype="int64") 
        self.array = self.a.tolist()
        for i in range(len(self.array)):
            self.t = tuple(self.array[i])
            self.g = [self.t]
            self.cg = self.c.SerialtoCoord(self.g, 8)
            self.scg = self.c.CoordtoSerial(self.cg, 8)
            self.assertEqual(self.g, list(self.scg))
    
    def test_onecase_inCoord(self):
        self.g = [((-1, 0), (0, 0)), ((-1, 0), (0, 1)), ((-1, 0), (0, 2)), ((0, 0), (1, 0)), ((0, 0), (1, 1)), ((1, 0), (2, 0)), ((1, 1), (2, 1))]
        self.sg = self.c.CoordtoSerial(self.g)
        self.csg = self.c.SerialtoCoord(self.sg)
        self.assertEqual(self.g, list(self.csg)) 

# 一般の座標表示g' と csg' の比較も書かなきゃいけない気がするけど、めんどいのでやりません。

if __name__ == "__main__":
    unittest.main()

