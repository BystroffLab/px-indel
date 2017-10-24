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


if __name__ == "__main__": main()