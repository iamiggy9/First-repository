import termcolor

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):

        # Initialize the sequence with the value

        # passed as argument when creating the object

        if Seq.is_valid_sequence_2(strbases):
             print("New sequence created!")
             self.strbases = strbases
        else:
            self.strbases = 'Error'
            print('INCORRECT Sequence detected')
    @staticmethod
    def is_valid_sequence_2(strbases):
        for c in strbases:
            if c!='A' and c !='C' and c!='G' and c!= 'T':
               return False
        return True
    @staticmethod
    def print_seqs(seq_list):
        for i in range(0, len(seq_list)):
            text='Sequence: ' + str(i) + " , (Lenght : " + str(seq_list[i].len()) + ")" + str(seq_list[i])
            termcolor.cprint(text,'blue')

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
        """Calculate the length of the sequence"""
        return len(self.strbases)


# --- Main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("te")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")