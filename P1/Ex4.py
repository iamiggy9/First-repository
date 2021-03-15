
from Seq1 import Seq

print("-----| Practice 1, Exercise 4 |------")

# -- Create a Null sequence
s1 = Seq('NULL')

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("ERROR")

print("Sequence 1: (Length : ", s1.len(), ")", s1)
print("Sequence 1: (Length : ", s2.len(), ")", s2)
print("Sequence 1: (Length : ", s3.len(), ")", s3)

