import numpy as np

def load_blosum62():
    """Return BLOSUM62 matrix as a dictionary"""
    # BLOSUM62 matrix (truncated for brevity, full matrix should be used)
    blosum62 = {
        'A': {'A': 4, 'R': -1, 'N': -2, 'D': -2, 'C': 0, 'Q': -1, 'E': -1, 'G': 0, 'H': -2, 'I': -1,
              'L': -1, 'K': -1, 'M': -1, 'F': -2, 'P': -1, 'S': 1, 'T': 0, 'W': -3, 'Y': -2, 'V': 0},
        # ... (完整矩阵应包含所有20种氨基酸)
        '*': {'*': 1, 'A': -4, 'R': -4, 'N': -4, 'D': -4, 'C': -4, 'Q': -4, 'E': -4, 'G': -4, 'H': -4,
              'I': -4, 'L': -4, 'K': -4, 'M': -4, 'F': -4, 'P': -4, 'S': -4, 'T': -4, 'W': -4, 'Y': -4, 'V': -4}
    }
    return blosum62

def read_fasta(filename):
    """Read a FASTA file and return header and sequence"""
    with open(filename) as f:
        header = f.readline().strip()[1:]
        sequence = ''.join(line.strip() for line in f)
    return header, sequence

def align_sequences(seq1, seq2, blosum):
    """
    Perform global non-gapped alignment and return:
    - alignment score
    - percentage identity
    - alignment visualization
    """
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must be of equal length for non-gapped alignment")
    
    score = 0
    matches = 0
    alignment1 = []
    alignment2 = []
    
    for a, b in zip(seq1, seq2):
        score += blosum.get(a, {}).get(b, -4)  # Default penalty -4 for invalid chars
        if a == b:
            matches += 1
        alignment1.append(a)
        alignment2.append(b)
    
    percent_identity = (matches / len(seq1)) * 100
    return score, percent_identity, (''.join(alignment1), ''.join(alignment2))

def main():
    # Load sequences
    human_header, human_seq = read_fasta("human_SOD2.fasta")
    mouse_header, mouse_seq = read_fasta("mouse_SOD2.fasta")
    random_header, random_seq = read_fasta("random_seq.fasta")
    
    # Load BLOSUM62 matrix
    blosum = load_blosum62()
    
    # Perform alignments
    print("\n=== Pairwise Sequence Comparisons ===")
    
    # Human vs Mouse
    hm_score, hm_identity, hm_aln1, hm_aln2 = align_sequences(human_seq, mouse_seq, blosum)
    print(f"\n1. Human vs Mouse\nScore: {hm_score}\nIdentity: {hm_identity:.1f}%")
    
    # Human vs Random
    hr_score, hr_identity, hr_aln1, hr_aln2 = align_sequences(human_seq, random_seq, blosum)
    print(f"\n2. Human vs Random\nScore: {hr_score}\nIdentity: {hr_identity:.1f}%")
    
    # Mouse vs Random
    mr_score, mr_identity, mr_aln1, mr_aln2 = align_sequences(mouse_seq, random_seq, blosum)
    print(f"\n3. Mouse vs Random\nScore: {mr_score}\nIdentity: {mr_identity:.1f}%")
    
    # Generate report
    with open("alignment_report.txt", "w") as report:
        report.write("=== Sequence Alignment Report ===\n")
        report.write(f"Human SOD2: {human_header}\nLength: {len(human_seq)} aa\n")
        report.write(f"Mouse SOD2: {mouse_header}\nLength: {len(mouse_seq)} aa\n")
        report.write(f"Random seq: {random_header}\nLength: {len(random_seq)} aa\n\n")
        
        report.write("Comparison Results:\n")
        report.write(f"1. Human vs Mouse\nScore: {hm_score}\nIdentity: {hm_identity:.1f}%\n\n")
        report.write(f"2. Human vs Random\nScore: {hr_score}\nIdentity: {hr_identity:.1f}%\n\n")
        report.write(f"3. Mouse vs Random\nScore: {mr_score}\nIdentity: {mr_identity:.1f}%\n\n")
        
        report.write("Conclusion:\n")
        if hm_identity > max(hr_identity, mr_identity):
            report.write("Human and mouse SOD2 show significant sequence similarity,\n")
            report.write(f"with {hm_identity:.1f}% identity, suggesting evolutionary conservation.")
        else:
            report.write("Unexpected result: Random sequence shows higher similarity\n")
            report.write("than biologically related sequences. Check input data.")

if __name__ == "__main__":
    main()
