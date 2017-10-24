from px_min import *
import Bio
import Bio.PDB
import sys
import unittest
import numpy as np
import shutil
import os
import os.path
from commands import getstatusoutput as run

def diff(a,b): return abs(a-b)

class test_px_min(unittest.TestCase):
    
    def setUp(self):
        self.parser = Bio.PDB.PDBParser()
        self.trpCage = self.parser.get_structure("trp-cage","testFiles/1L2Y.pdb")
        
    def test_genCoordinates(self):
        output = [(atom,coords) for (atom,coords) in genCoordinates(self.trpCage,"A",7)]
        self.assertEqual(len(output),19)
        self.assertEqual(output[0][0],"N")
        self.assertTrue(diff(output[0][1][0],np.float(-1.600))<0.0001)
        self.assertTrue(diff(output[0][1][1],np.float(-1.860))<0.0001)
        self.assertTrue(diff(output[0][1][2],np.float(0.967))<0.0001)
        self.assertEqual(output[7][0],"CD2")
        self.assertTrue(diff(output[7][1][1],np.float(-2.007))<0.0001)
        
class test_genSymmetry(unittest.TestCase):
    
    def tearDown(self):
        shutil.rmtree("testFiles/SymmTest")
        os.mkdir("testFiles/SymmTest")
        shutil.copy("testFiles/symtest.pdb","testFiles/SymmTest")
        
    def test_scriptRuns(self):
        self.assertTrue(genSymmetry("testFiles/SymmTest/symtest.pdb"))
        
    def test_Files_output(self):
        stem = "testFiles/SymmTest/symtest"
        genSymmetry("testFiles/SymmTest/symtest.pdb")
        self.assertTrue(os.path.isfile("%s_INPUT.pdb"%(stem)))
        self.assertTrue(os.path.isfile("%s_model_AB.pdb"%(stem)))
        self.assertTrue(os.path.isfile("%s_symm.pdb"%(stem)))
        self.assertTrue(os.path.isfile("%s.kin"%(stem)))
        
if __name__ == "__main__": unittest.main()