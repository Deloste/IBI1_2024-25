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
    """Extracts just the gene name from a FASTA header."""
    parts = header_line.split()
    return parts[0][1:]

tata_regex = re.compile(r'TATA[AT]A[AT]')

# Splice site dictionary for user convenience
# E.g. 'GTAG' means donor is GT, acceptor is AG
splice_sites = {'GTAG': ('GT', 'AG'), 'GCAG': ('GC', 'AG'), 'ATAC': ('AT', 'AC')}
valid_choices = list(splice_sites.keys())

# 1. Ask user for splice site combination
user_input = input(f"Choose splice donor/acceptor combination [{', '.join(valid_choices)}]: ").strip().upper()
while user_input not in valid_choices:
    user_input = input(f"Invalid. Please choose from {valid_choices}: ").strip().upper()

donor, acceptor = splice_sites[user_input]
output_file = f"{user_input}_spliced_genes.fa"
input_fasta = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"

with open(output_file, "w") as out:
    for header, seq in fasta_iter(input_fasta):
        # A "spliced gene" contains at least one donor-acceptor site (in order, donor before acceptor, both included)
        # Find all non-overlapping introns
        intron_pattern = re.compile(f'{donor}.*?{acceptor}')
        if intron_pattern.search(seq):
            tata_matches = tata_regex.findall(seq)
            if tata_matches:
                gene = get_gene_name(header)
                tata_count = len(tata_matches)
            
                out.write(f">{gene} TATA_box_count={tata_count}\n{seq}\n")
