<h1>Classify Sequence and Search for Motif </h1>
A Python script to classify an input sequence as either DNA or RNA and search for a given motif in the sequence (if provided).

<h3>Getting Started</h3>
These instructions will help you run the script on your local machine.

<h3>Prerequisites</h3>
You will need to have Python installed on your machine.

<h3>Installing</h3>
No installation is necessary, as this is a standalone script.

<h3>Running the Script</h3>
The script can be run from the command line with the following arguments:

* -s or --seq: the input sequence (required)
* -m or --motif: the motif to search for in the input sequence (optional)

<h3>Example:</h3>

```
python classify_sequence.py -s ACTG -m ACT
```

<h3>Functionality</h3>
The script uses the sys, re, and argparse modules to classify the input sequence and search for the given motif (if provided). The ArgumentParser class is used to handle the command line arguments and parse the input sequence and motif.

The input sequence is converted to uppercase and then checked against a regular expression to determine if it is composed of valid DNA or RNA nucleotides (ACGTU). If the input sequence is valid, the script checks if it contains either thymine (T) or uracil (U) and prints the appropriate message. If the input sequence contains invalid characters, the script prints a message indicating that the sequence is not DNA or RNA.

If the args.motif argument was provided, the motif is converted to uppercase and searched for in the input sequence using a regular expression. The script then prints the result of the search (found or not found).

<h2>Built With</h2>
Python - The programming language used

<h2>Author</h2>
Sergi Soldevila
