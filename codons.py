def create_codon_dict(file_path):
    pass # Replace the pass with your codedef create_codon_dict(file_path):
    path="data/codons.txt"
    file=open(path)
    rows=file.readlines()
    file.close()
    amino_acid_dict = {}
    for row in rows:
        row_cells = row.strip().split('\t')
        codon = row_cells[0]
        amino_acid = row_cells[2]
        amino_acid_dict[codon] = amino_acid
    return amino_acid_dict

