import unittest
from graphillion import GraphSet
from tree_univ import MakeUniverse, DrawGraph, OperationtoTrees
from ChangeCoord import ChangeCoordandSerial


class TestChanging(unittest.TestCase):
    def setUp(self):
        
        self.c = ChangeCoordandSerial()       

    def test_inSerial(self):
        with open("edges.txt", mode="r") as self.f:
            for self.line in self.f:
                self.g = self.line.replace("\n", "")
                self.cg = self.c.SerialtoCoord(self.g, 8)
                self.scg = self.c.CoordtoSerial(self.cg, 8)
                self.assertEqual(self.g, list(self.scg))


'''
    def test_inSerial(self):
        self.g = [(0, 1), (0, 2), (0, 3), (1, 8), (1, 9), (8, 15), (9, 16)] #self.graphset.choice()
        self.cg = self.c.SerialtoCoord(self.g)
        self.scg = self.c.CoordtoSerial(self.cg)
        self.assertEqual(self.g, list(self.scg))
'''


if __name__ == "__main__":
    unittest.main()
