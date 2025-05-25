# tata_genes.py

import re

def fasta_iter(fasta_filename):
    """Generator to yield (header, sequence) tuples from a FASTA file."""
    with open(fasta_filename) as fh:
        header = None
        seq_lines = []
        for line in fh:
            line = line.rstrip()
            if line.startswith(">"):
                if header:
                    yield (header, "".join(seq_lines))
                header = line
                seq_lines = []
            else:
                seq_lines.append(line)
        if header:
            yield (header, "".join(seq_lines))

def get_gene_name(header_line):
    """Extract gene name (first word after '>') from a FASTA header line."""
    # Example: >ENST00000632684 gene:xxx ...
    parts = header_line.split()
    gene = parts[0][1:]  # Remove '>'
    return gene

# TATA box regex: TATAWAW (W=A/T)
tata_regex = re.compile(r'TATA[AT]A[AT]')

input_fasta = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_fasta = "tata_genes.fa"

with open(output_fasta, "w") as out:
    for header, seq in fasta_iter(input_fasta):
        if tata_regex.search(seq):
            gene = get_gene_name(header)
            out.write(f">{gene}\n{seq}\n")
