from Seq0 import *
FOLDER = "../SESSION 4/"
FILENAME = "U5.txt"
print('----- | Exercise 2| ------')
print("DNA file: ", FILENAME)
print("The first 20 bases are: \n", seq_read_fasta(FOLDER+FILENAME)[:20])