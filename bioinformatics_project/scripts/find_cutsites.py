import sys

def read_fasta_file(filepath):
    """Read a FASTA file and return the DNA sequence as a single string."""
    sequence = [] # Initialize an empty list to store each line of the DNA sequence read from the file
    with open(filepath, 'r') as fasta_file: # Open the file per filepath and read ('r') it line by line; 'with' ensures that the file is properly closed after reading
        for line in fasta_file: # Loop over each line in the FASTA file
            sequence.append(line.strip()) # Strip whitespace and append to the list
    return ''.join(sequence) # Join the list of lines into a single string

def find_cut_sites(sequence, cutsite):
    """Find all occurrences of the cutsite in the DNA sequence."""
    cutsite = cutsite.replace('|', '') # Replace the character "|" with an empty string '' in the cutsite string
    cut_positions = [] # Initialize an empty list to store cutsite positions
    position = sequence.find(cutsite) # Find the first occurrence of the cutsite in the sequence
    while position != -1: # If position == -1, then it means the cutsite was not found in the sequence, and the loop will terminate
        cut_positions.append(position) # Append each cut position to the cut_positions list
        position = sequence.find(cutsite, position + 1) # Search for the next cutsite after each cutsite discovery
    return cut_positions # The total list of cut positions

def find_cut_pairs(cut_positions, min_distance = 80_000, max_distance = 120_000):
    """Find pairs of cut sites that are between min_distance and max_distance apart."""
    cut_pairs = [] # Initialize an empty list to store pairs of cutsites with the qualified distance in between
    for i in range(len(cut_positions)): # The outer loop iterates over each cutsite position
        for j in range(i + 1, len(cut_positions)): # The inner loop compares the current cutsite (i) with the subsequent cutsite (j=i+1)
            distance = cut_positions[j] - cut_positions[i]
            if min_distance <= distance <= max_distance:
                cut_pairs.append((cut_positions[i], cut_positions[j]))
    return cut_pairs

if __name__ == '__main__':
    # Get the input file path and cutsite from the command-line arguments
    if len(sys.argv) < 3:
        print("Usage: python find_cutsites.py <FASTA file> <cutsite>")
        sys.exit(1)
    
    fasta_file = sys.argv[1]
    cutsite = sys.argv[2]

    # Read the DNA sequence from the FASTA file
    dna_sequence = read_fasta_file(fasta_file)

    # Find all cut sites in the sequence
    cut_positions = find_cut_sites(dna_sequence, cutsite)

    # Find pairs of cut sites that are 80-120 kbp apart
    cut_pairs = find_cut_pairs(cut_positions)

    # Print the total number of pairs 80-120 kbp apart found and the first 5 pairs
    print(f"Total cut site found: {len(cut_positions)}")
    print(f"Cut site pairs 80-120 kbp apart: {len(cut_pairs)}")
    print(f"First 5 pairs:")
    for pair in cut_pairs[:5]:
        print(f"{pair[0]} - {pair[1]}")
    
    # Save the results to the summary file
    with open('bioinformatics_project/results/cutsite_summary.txt', 'w') as summary_file: # 'w' = write mode, creates the file if it doesn't already exist or overwrites it if it does
        summary_file.write(f"Analyzing cut site: {cutsite}\n")
        summary_file.write(f"Total cut sites found: {len(cut_positions)}\n")
        summary_file.write(f"Cut site pairs 80-120 kbp apart: {len(cut_pairs)}\n")
        summary_file.write("First 5 pairs:\n")
        for index, pair in enumerate(cut_pairs[:5], start=1): # Use enumerate to add numbering for list items as exemplified
            summary_file.write(f"{index}. {pair[0]} - {pair[1]}\n")
    
    print("Results saved to bioinformatics_project/results/cutsite_summary.txt")
