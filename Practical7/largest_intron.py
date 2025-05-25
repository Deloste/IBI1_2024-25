# largest_intron.py

seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

# Find all GT...AG introns, where both GT and AG are included in the intron
import re

def largest_intron_length(seq):
    intron_pattern = re.compile(r'GT.*?AG')
    introns = [m.group() for m in intron_pattern.finditer(seq)]
    if not introns:
        print("No introns found.")
        return 0
    largest = max(len(intron) for intron in introns)
    return largest

# Print the largest intron length
print(largest_intron_length(seq))
