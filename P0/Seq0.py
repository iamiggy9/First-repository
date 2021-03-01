from pathlib import Path



def seq_ping():
    print('OK')
def take_out_first_line(seq):
    return seq[seq.find('\n') + 1:].replace('\n', '')
def seq_read_fasta(filename):
     sequence = take_out_first_line(Path(filename).read_text())
     return sequence
def seq_len(seq):
    return len(seq)
def seq_count_base(seq,base):