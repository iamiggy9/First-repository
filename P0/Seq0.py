from pathlib import Path



def seq_ping():
    print('OK')


def take_out_first_line(seq):
    return seq[seq.find('\n') + 1:].replace('\n', '')
def seq_read_fasta(filename):
     sequence = Path(filename).read_text()
     contain =sequence.split('\n')
     contain=contain[1:]
     final_string= ''.join(contain)
     return final_string


def seq_len(seq):
    return len(seq)


def seq_count_base(seq,base):
    counter = 0
    for e in seq:
        if e in base:
            counter += 1
        return counter

def seq_count(seq):
    bases = ["A", "C", "T", "G"]
    count_bases = []
    for base in bases:
        count_bases.append(seq_count_base(seq, base))
    dictionary = dict(zip(bases, count_bases))
    return dictionary

def seq_reverse(seq):
    reverse_sequence = ''
    for e in seq[::-1]:
        reverse_sequence += e
    return (reverse_sequence)


def seq_complement(seq):
    bases = ["A", "C", "T", "G"]
    bases_comp = ["T", "G", "A", "C"]
    comp_seq = ""
    dict_comp = dict(zip(bases, bases_comp))
    for e in seq:
        for i, t in dict_comp.items():
            if e == i:
                comp_seq += t
    return (comp_seq)


