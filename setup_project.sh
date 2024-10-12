#!/bin/bash
mkdir -p bioinformatics_project/{data,scripts,results}
touch bioinformatics_project/scripts/{generate_fasta.py,dna_operations.py,find_cutsites.py}
touch bioinformatics_project/results/cutsite_summary.txt
touch bioinformatics_project/data/random_sequence.fasta
echo "This bioinformatics project is Ziqian's DATASCI217 Exam 1. It has the following structure:
- DATA contains input data like FASTA files; 
- SCRIPTS contains Python scripts that handle the DNA sequence operations; and 
- RESULTS results contains operation outputs like cutsite summary.
" > bioinformatics_project/README.md
echo "Project directory structure created successfully."
