from Seq_1 import Seq
import termcolor

seq_list1 = Seq.generate_seqs("A", 3)
seq_list2 = Seq.generate_seqs("AC", 5)

termcolor.cprint("List 1:",'blue')
print(Seq.print_seqs(seq_list1))

termcolor.cprint("List 2:",'yellow')
print(Seq.print_seqs(seq_list2))

