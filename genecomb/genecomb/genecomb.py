from operator import ge
import re


class GeneComb:
    def __init__(self, seq='', header=''):
        self.seq = seq
        self.header = header

    def base_counter(self):
        """This function returns count of all bases in a sequence as a dictionary
        Ex: ACGGGTAC -> {'A': 2, 'C': 2, 'G': 3, 'T': 1}
        Parameters:
            seq (str): nucleotide sequence
        Returns:
            returns the count of all bases as a dictionary
        """
        base_count = {"A": 0, "C": 0, "G": 0, "T": 0, "X": 0}

        for i in self.seq:
            if i == "A":
                base_count["A"] += 1
            elif i == "G":
                base_count["G"] += 1
            elif i == "C":
                base_count["C"] += 1
            elif i == "T":
                base_count["T"] += 1
            else:
                base_count["X"] += 1

        return base_count

    def gc_content(self):
        """This function returns the GC content of a sequence.
        Ex: If the sequence is 100 bases long and you have 20 C’s and 5 G’s, your GC content is 25%
        Parameters:
            seq (str): nucleotide sequence
        Returns:
            returns the GC content
        """
        base_dict = self.base_counter()
        base_count = len(self.seq)
        gc_count = base_dict.get("C") + base_dict.get("G")
        try:
            gc_content = gc_count / base_count
        except ZeroDivisionError:
            print(
                "Tried to divide by 0: Sequence is most likely empty. Returning 0 instead"
            )
            return 0
        return round(gc_content, 2)

    def non_nucleotide_counter(self):
        """This function parses a sequence and returns a list of the location of each
        non ACGT base and the length of unknown bases if they are consecutive
        Ex: ACNGGGNNNTAC -> [[2, 2],[6, 8]]
        Parameters:
            seq (str): nucleotide sequence
        Returns:
            returns dictionary in the form of {position: length}
        """
        non_nucleotides = []

        match = re.finditer(r"[^ATCG]{1,}", self.seq)
        for i in match:
            non_nucleotides.append([i.start(), i.end() - 1])
        return non_nucleotides

    def find_palindromes(self, removeOverlap=False):
        """This function parses the sequence and returns a list of palindromic nucleotide sequences
        within the seq.
        Parameters:
            seq (str): sequence
        Returns:
            Returns a list of all the palindromes. Each entry in the list is another with the start position at index 0
            and the end position at index 1
        """

        palindromes = []
        seq = self.seq
        # recursive function called in find_palindromes()
        def expand(low, high):
            """
            Helper function for finding palindromes
            """

            # run till `s[low.high]` is not a palindrome
            while (
                low >= 0
                and high < len(seq)
                and compare_complimentary(seq[low], seq[high])
            ):
                # update pointers
                low = low - 1
                high = high + 1

            # seq must be length of 3 or longer
            if high - low > 1:
                palindromes.append([low + 1, high - 1])

        def remove_nested_palindromes():
            """
            Helper function to remove palindromes that overlap.
            """
            current_max = palindromes[0][1]
            remove_list = []
            for i in range(len(palindromes)):
                if palindromes[i][0] <= current_max:
                    remove_list.append(palindromes[i])
                else:
                    current_max = palindromes[i][1]
            for item in remove_list:
                palindromes.remove(item)
            return palindromes

        def compare_complimentary(a, b):
            """
            Helper function to compare if two bases are complementary
            Parameters:
                a (str): first base
                b (str): second base
            Returns:
                Returns True if a and b are complimentary
            """
            if a == "A":
                return b == "T"
            elif a == "T":
                return b == "A"
            elif a == "C":
                return b == "G"
            elif a == "G":
                return b == "C"
            else:
                return False

        for i in range(len(seq)):

            # odd length strings
            expand(i, i)
            # even length strings
            expand(i, i + 1)

        # print all unique palindromic substrings
        if removeOverlap and len(palindromes) != 0:
            return remove_nested_palindromes()
        return palindromes

    def write_to_fasta_file(self, filepath, append=False):
        '''Writes the sequence and header to a file in the FASTA format'''
        with open(filepath, 'w') as file:
            file.write(self.header + '\n')
            for i in range(0,len(self.seq),80):
                file.write(self.seq[i:i+80] + '\n')
            file.write('\n')
            



def read_fasta(filename):
    ''' Reads a .fasta file and returns a list of GeneComb objects. Each object corresponding to each sequence in the file'''
    genecomb_list = []
    current_genecomb = GeneComb()
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            if line[0] == '>':
                if len(genecomb_list) != 0:
                    current_genecomb = GeneComb()
                genecomb_list.append(current_genecomb)
                current_genecomb.header += line[:-1] 
            else:
                current_genecomb.seq += line[:-1]
    if len(genecomb_list) == 1:
        return genecomb_list[0]
    elif len(genecomb_list) == 0:
        return GeneComb()
    else: 
        return genecomb_list

            



