import pathlib


class Seq:
    """A class for representing sequence objects"""

    def __init__(self, strbases="NULL"):  # by default the Seq object is NULL
        if strbases == "NULL":
            print("NULL Seq Created")
            self.strbases = "NULL"
            self.length = 0  # If the sequence is null the length is = 0
        else:
            valid = True
            i = 0
            while i < len(strbases) and valid:
                # Look for incorrect bases
                if (strbases[i] != "A") and (strbases[i] != "C") and (strbases[i] != "G") and (strbases[i] != "T"):
                    valid = False
                    self.strbases = "ERROR"
                    self.length = 0  # If the sequence is not valid the length is = 0
                    print("INVALID Seq!")
                else:
                    i += 1

            if valid and strbases != "NULL":  # The sequence is valid !!
                print("New sequence created!")
                self.strbases = strbases
                self.length = len(self.strbases)
    @staticmethod
    def is_valid_sequence_2(strbases):
        for c in strbases:
            if c!='A' and c !='C' and c!='G' and c!= 'T':
               return False
        return True
    @staticmethod
    def print_seqs(seq_list):
        for i in range(0, len(seq_list)):
            if [i]=='NULL':
                text = 'Sequence: ' + str(i) + " , (Lenght : 0 "  +  str(seq_list[i])
                print(text)
            if [i]=='ERROR':
                text = 'Sequence: ' + str(i) + " , (Lenght : 0 " + str(seq_list[i])
                print(text)
            else:
                text='Sequence: ' + str(i) + " , (Lenght : " + str(seq_list[i].len()) + ")" + str(seq_list[i])
                print(text)

    @staticmethod
    def generate_seqs(pattern, number):
        empty_list=[]
        for i in range(0,number):
            empty_list.append(Seq(pattern * (i+1)))
        return empty_list








    def is_valid_sequence(self):
        for c in self.strbases:
            if c!='A' and c !='C' and c!='G' and c!= 'T':
               return False
        return True


    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        return self.length

    def count_base(self, base):
        return self.strbases.count(base)

    def count(self):
        bases = ["A", "C", "T", "G"]
        count_bases = []
        for base in bases:
            count_bases.append(self.count_base(base))
        dictionary = dict(zip(bases, count_bases))
        return dictionary

    @staticmethod
    def reverse(self):
        rev_seq = ''
        if self.strbases == 'NULL':
            return self.strbases
        else:
            for e in self.strbases[::-1]:
                if e not in ["A", "C", "T", "G"]:
                    rev_seq = 'ERROR'
                    return rev_seq

                else:
                    rev_seq += e
        return rev_seq
    @staticmethod
    def complement(self):
        comp_seq = ""
        if self.strbases == 'NULL':
            return self.strbases
        else:
            for e in self.strbases:
                if e not in ["A", "C", "T", "G"]:
                    comp_seq = 'ERROR'
                    return comp_seq
                else:
                    if e in "A":
                        comp_seq += "T"
                    if e in "T":
                        comp_seq += "A"
                    if e in "C":
                        comp_seq += "G"
                    if e in "G":
                        comp_seq += "C"
            return (comp_seq)

    def read_fasta(self, filename):
            file_lines = pathlib.Path(filename).read_text().split("\n")
            body = (file_lines[1:])
            self.strbases = ''.join(body)
            return (self)

    pass

    def read_file_lines(filename):
        file_lines = pathlib.Path(filename).read_text().split("\n")
        body = (file_lines[1:])
        sp_list = []
        for e in body:
            e = e.split(',')
            fin_str = e[0]
            sp_list.append(fin_str)
        return (sp_list)