import unittest
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
sys.path.append(str(Path(__file__).parent.parent / "forLocal"))

import forLocal.ChangeCoord.ChangeCoordandSerial
# from forLocal.ChangeCoord import Changehogehoge

from graphillion import GraphSet


'''class TestChanging(unittest.TestCase):
    def setUp(self):
        
        self.c = ChangeCoord.ChangeCoordandSerial()       

    def test_onecase(self):
        self.g = [(0, 1), (0, 2), (0, 3), (1, 8), (1, 9), (8, 15), (9, 16)] 
        self.cg = self.c.SerialtoCoord(self.g)
        self.scg = self.c.CoordtoSerial(self.cg)
        self.assertEqual(self.g, list(self.scg))

    def test_inSerial(self):
        with open("edges.txt", mode="r") as self.f:
            for self.line in self.f:
                self.g = self.line.replace("\n", "")
                self.cg = self.c.SerialtoCoord(self.g, 8)
                self.scg = self.c.CoordtoSerial(self.cg, 8)
                self.assertEqual(self.g, list(self.scg))
'''


# if __name__ == "__main__":
#    unittest.main()

print(Path(__file__))
# print(sys.path)