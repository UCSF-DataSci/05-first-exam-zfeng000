import sys

def complement(sequence):
    """Return the complement of a DNA sequence."""
    complement_map = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return ''.join(complement_map[base] for base in sequence)

def reverse(sequence):
    """Return the reverse of a DNA sequence."""
    return sequence[::-1] # the slicing notation that reverses a string

def reverse_complement(sequence):
    """Return the reverse complement of a DNA sequence."""
    return reverse(complement(sequence))

if __name__ == '__main__': # check to see that a DNA sequence is a command-line argument
    if len(sys.argv) < 2:
        print("Please provide a DNA sequence.")
        sys.exit(1) # exist the script with an error code if no DNA sequence is provided

    dna_sequence = sys.argv[1].upper() # upper() converts to all uppercases

    print(f"Original sequence: {dna_sequence}")
    print(f"Complement: {complement(dna_sequence)}")
    print(f"Reverse: {reverse(dna_sequence)}")
    print(f"Reverse complement: {reverse_complement(dna_sequence)}")