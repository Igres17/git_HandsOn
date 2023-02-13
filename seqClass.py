#!/usr/bin/env python

# Import the sys and re modules, as well as the ArgumentParser class from the argparse module
import sys
import re
from argparse import ArgumentParser

# Create an ArgumentParser object to handle command line arguments
parser = ArgumentParser(description="Classify a sequence as DNA or RNA")

# Add the required argument "seq" for the input sequence
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")

# Add an optional argument "motif" for the motif to search for in the sequence
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

# If no arguments are provided, print the help message and exit the script
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse the command line arguments
args = parser.parse_args()

# Convert the input sequence to upper case
args.seq = args.seq.upper()

# Check if the input sequence is composed of valid DNA or RNA nucleotides
if re.search("^[ACGTU]+$", args.seq):
    # Check if the input sequence contains the nucleotide thymine (T), indicating that it is DNA
    if re.search("T", args.seq):
        print("The sequence is DNA")
    # Check if the input sequence contains the nucleotide uracil (U), indicating that it is RNA
    elif re.search("U", args.seq):
        print("The sequence is RNA")
    # If neither T nor U are present, the sequence could be either DNA or RNA
    else:
        print("The sequence can be DNA or RNA")
# If the input sequence contains invalid characters, it is not DNA or RNA
else:
    print("The sequence is not DNA nor RNA")

# Check if the motif argument was provided
if args.motif:
    # Convert the motif to upper case
    args.motif = args.motif.upper()
    # Search for the motif in the input sequence
    print(
        f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ',
        end="",
    )
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")
