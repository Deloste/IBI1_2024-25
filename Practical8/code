# Drug dosage calculator function

def paracetamol_volume(weight_kg, strength_str):
    """
    Calculate paracetamol volume (ml) based on weight and strength string.
    Parameters:
        weight_kg (float): Patient weight in kg. Must be 10–100.
        strength_str (str): Must be '120 mg/5 ml' or '250 mg/5 ml'.
    Returns:
        float: Dose volume in ml.
    Raises:
        ValueError: on invalid weight or strength.
    """
    if not (10 <= weight_kg <= 100):
        raise ValueError("Weight must be between 10 and 100 kg")
    if strength_str == '120 mg/5 ml':
        mg_per_ml = 120 / 5
    elif strength_str == '250 mg/5 ml':
        mg_per_ml = 250 / 5
    else:
        raise ValueError("Strength must be '120 mg/5 ml' or '250 mg/5 ml'")
    dose_mg = 15 * weight_kg
    volume_ml = dose_mg / mg_per_ml
    return volume_ml

# Example usage:
try:
    dose = paracetamol_volume(20, '250 mg/5 ml')
    print(f"Example: Give {dose:.2f} ml paracetamol")
except ValueError as err:
    print("Error:", err)

# Patient record management class

class Patient:
    """
    Represents a patient and can output a summary of patient details.
    """
    def __init__(self, name, age, admission_date, medical_history):
        self.name = name
        self.age = age
        self.admission_date = admission_date
        self.medical_history = medical_history

    def print_record(self):
        """
        Prints all patient record information in a single line.
        """
        print(f"{self.name}, {self.age}, {self.admission_date}, {self.medical_history}")

# Example usage:
p = Patient("Alex Smith", 12, "2023-09-01", "Asthma, no known allergies")
p.print_record()

# Restriction enzyme cut sites

def find_restriction_sites(dna_seq, enzyme_seq):
    """
    Find start positions of all occurrences of enzyme_seq (restriction site) in dna_seq.
    Both sequences must be A/C/G/T only (case-insensitive).
    Returns a list of integer indices (0-based).
    Raises ValueError if input is not valid DNA.
    """
    dna_seq = dna_seq.upper()
    enzyme_seq = enzyme_seq.upper()
    if not (set(dna_seq) <= set('ACGT')) or not (set(enzyme_seq) <= set('ACGT')):
        raise ValueError("Sequences must contain only A, C, G, or T")
    positions = []
    pos = dna_seq.find(enzyme_seq)
    while pos != -1:
        positions.append(pos)
        pos = dna_seq.find(enzyme_seq, pos + 1)
    return positions

# Example usage:
try:
    cuts = find_restriction_sites("GAATTCCGGGAATTCCAATTCAAGGAATTCAA", "GAATTC")
    print("Example: Cut sites at positions:", cuts)
except ValueError as err:
    print("Error:", err)

# End of portfolio script
