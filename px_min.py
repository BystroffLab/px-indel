import optparse
import Bio
import Bio.PDB
from rosetta import *

def main():
    parser = optparse.OptionParser()
    # pdb input option
    parser.add_option("-f","--file",dest="pdb",help="Input PDB file to be energy minimized",metavar="in.pdb")
    # pdb output option
    parser.add_option("-o","--out",dest="outFile",help="Filename of minimized PDB to be output",metavar="out.pdb")
    # Alanine insertion location option
    parser.add_option("-a","--Ala",type="int",dest="alaRegions",nargs=4,help="Beginning and end residue numbers for both polyA regions of T7 endoI",metavar="ABeg AEnd BBeg BEnd")
    parser.add_option("-c","--cst",dest="cst",help="cst file in which to save constraints",metavar="constraints.cst",default="constraints.cst")
    
    (options,args) = parser.parse_args()
    
    PdbIn = options["pdb"]
    PdbOut = options["outFile"]
    AlaReg1 = options["alaRegions"][:2]
    AlaReg2 = options["alaRegions"][2:]
    
    
    
def addConstraints(isPx = False):
    None
    PXChains = ["C","D","E","F"]
    
def genSymmetry():
    ''' Generate the symmetry files for use in rosetta '''
    None

def runMinimization():
    None

def genCoordinates(structure,chain,resNum):
    '''Generator that yields atom name and spacial coordinates for each atom in
    a given residue'''
    for atom in structure[0][chain][resNum].get_atoms():
        yield (atom.get_id(),atom.get_coord())

if __name__ == "__main__": main()