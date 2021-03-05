from pathlib import Path


def seq_ping():
    print('OK')

def is_valid_sequence(strbases):
        for c in strbases:
            if c!='A' and c !='C' and c!='G' and c!= 'T':
               return False
        return True
def take_out_first_line(seq):
    return seq[seq.find('\n') + 1:].replace('\n', "")


def seq_read_fasta(filename):
    sequence = take_out_first_line(Path(filename).read_text())
    return sequence


def seq_len(seq):
    return len(seq)


def seq_count_base(seq, base):
    return seq.count(base)


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
    return reverse_sequence


def seq_complement(seq):
    bases = ["A", "C", "T", "G"]
    bases_comp = ["T", "G", "A", "C"]
    comp_seq = ""
    dict_comp = dict(zip(bases, bases_comp))
    for e in seq:
        for i, t in dict_comp.items():
            if e == i:
                comp_seq += t
    return comp_seq