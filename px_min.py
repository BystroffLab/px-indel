import optparse
import Bio
import Bio.PDB
import sys
# from commands import getstatusoutput as run
import subprocess
# from rosetta import *

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
    
    
    
def addConstraints(structure,region1,region2):
    PXChains = ["C","D","E","F"]
    constraints = []
    # Get PX CoordinateConstraints
    for chain in PXChains:
        for res in structure[0][chain]:
            for (atom,(x,y,z)) in genCoordinates(structure,chain,res):
                # CoordinateConstraint atom res atom2 res2 x y z HARMONIC x0 sd
                constraint = "CoordinateConstraint %s %i%c N 1A %f %f %f HARMONIC 1.0 0.1"%(atom,res,chain,x,y,z)
                constraints.append(constraint)
    #generate beta-beta constraints between region1 and region2            
    return constraints
    
    
def genSymmetry(pdb,m='NCS',a='A',i='B',d='C D E F'):
    ''' Generate the symmetry files for use in rosetta.  calls the
    make_symmdef_file.pl script'''
    # perl make_symmdef_file.pl -m NCS -a A -i B -p filename
    script = "make_symmdef_file.pl"
    out = pdb.split(".pdb")[0] + ".symm"
    cmd = ["perl",script,'-m',m,'-a',a,'-i',i,'-d',d,'-p',pdb]
    p = subprocess.Popen(cmd,stdout = subprocess.PIPE,stderr=subprocess.PIPE)
    (stdoutdata,stderrdata) = p.communicate()
    out = open("%s.symm"%(pdb.split(".pdb")[0]),"w+")
    out.write(stdoutdata)
    out.close()
    if p.returncode != 0: return False
    return True

def runMinimization():
    None

def genCoordinates(structure,chain,resNum=0):
    '''Generator that yields atom name and spacial coordinates for each atom in
    a given residue'''
    if resNum != 0:
        for atom in structure[0][chain][resNum].get_atoms():
            yield (atom.get_id(),atom.get_coord())
    else:
        for res in structure[0][chain]:
            for atom in res:
                yield(atom.get_id(),atom.get_coord())

if __name__ == "__main__": main()