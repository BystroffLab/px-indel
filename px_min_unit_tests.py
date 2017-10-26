from px_min import *
import Bio
import Bio.PDB
import sys
import unittest
import numpy as np
import shutil
import os
import os.path
import StringIO
from commands import getstatusoutput as run

def diff(a,b): return abs(a-b)

class test_px_min(unittest.TestCase):
    
    def setUp(self):
        parser = Bio.PDB.PDBParser()
        self.trpCage = parser.get_structure("trp-cage","testFiles/1L2Y.pdb")
        
    def test_genCoordinates(self):
        # We need to use a tolerance because BioPython adds a little nonsense to
        # the ends of the coordinates (numpy float32)
        tolerance = 0.000001
        output = [(atom,coords) for (atom,coords) in genCoordinates(self.trpCage,"A",7)]
        self.assertEqual(len(output),19)
        self.assertEqual(output[0][0],"N")
        self.assertTrue(diff(output[0][1][0],np.float32(-1.600)) <= tolerance)
        self.assertTrue(diff(output[0][1][1],np.float32(-1.860)) <= tolerance)
        self.assertTrue(diff(output[0][1][2],np.float32(0.967)) <= tolerance)
        self.assertEqual(output[7][0],"CD2")
        self.assertTrue(diff(output[7][1][1],np.float(-2.007)) <= tolerance)
        
class test_genSymmetry(unittest.TestCase):
    
    def tearDown(self):
        shutil.rmtree("testFiles/SymmTest")
        os.mkdir("testFiles/SymmTest")
        shutil.copy("testFiles/symtest.pdb","testFiles/SymmTest")
        
    def test_scriptRuns(self):
        self.assertTrue(genSymmetry("testFiles/SymmTest/symtest.pdb"))
        
    def test_filesOutput(self):
        stem = "testFiles/SymmTest/symtest"
        genSymmetry("testFiles/SymmTest/symtest.pdb")
        self.assertTrue(os.path.isfile("%s_INPUT.pdb"%(stem)))
        self.assertTrue(os.path.isfile("%s_model_AB.pdb"%(stem)))
        self.assertTrue(os.path.isfile("%s_symm.pdb"%(stem)))
        self.assertTrue(os.path.isfile("%s.kin"%(stem)))
        self.assertTrue(os.path.isfile("%s.symm"%(stem)))
        
class test_makeBlueprint(unittest.TestCase):
    
    def setUp(self):
        self.blueprint = StringIO.StringIO()
        
    def tearDown(self):
        self.blueprint.close()
        
    def test_empty(self):
        makeBlueprint(self.blueprint,(0,0))
        self.assertEqual(self.blueprint.getvalue(),"")
        
    def test_range(self):
        makeBlueprint(self.blueprint,(10,30))
        blueprint = self.blueprint.getvalue().split("\n")
        i = 10
        for line in blueprint:
            if i == 31: targetString = ""
            else: targetString = "%i A E ALLAA"%(i)
            self.assertEqual(line,targetString)
            i += 1
            
    def test_one(self):
        makeBlueprint(self.blueprint,(1,1))
        self.assertEqual(self.blueprint.getvalue(),"1 A E ALLAA\n")

if __name__ == "__main__": unittest.main()