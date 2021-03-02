from P0.Seq0 import *
FOLDER = "../SESSION 4/"
GENENAME = "U5"
first_bases = seq_read_fasta(FOLDER+GENENAME+'.txt')[:20]
print("Gene ", GENENAME, ":")
print("Frag: ", first_bases)
print("Comp : ",seq_complement(first_bases))