import random

def gen_random_dna_sequence(length): 
    """generate a random DNA sequence for a specified length"""
    return ''.join(random.choice('ACGT') for _ in range(length))

def write_fasta_file(filename, sequence, line_length = 80):
    """write the DNA sequence to a FASTA file with the specified line length"""
    with open(filename, 'w') as fasta_file:
        for i in range(0, len(sequence), line_length):
            fasta_file.write(sequence[i:i+line_length] + '\n')

# use the defined function to generate the random dna sequence of 1 million base pairs
random_sequence = gen_random_dna_sequence(1_000_000)

# write the resulting sequence to the empty FASTA file
write_fasta_file('bioinformatics_project/data/random_sequence.fasta', random_sequence)

print("Random RNA sequence generated and saved to ./random_sequence.fasta")