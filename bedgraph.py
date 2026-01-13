def reverse(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(seq))


def palindrome_check(seq, max_mismatches = 2):
    rev = reverse(seq)
    mismatches = 0
    for i in range(len(seq)):
        if seq[i] != rev[i]:
            mismatches += 1
            if mismatches > max_mismatches:
               return False
    return True


def find_palindromes(sequence, min_length = 5, max_length = 10, max_mismatches = 2):
    palindromes = []
    for length in range(min_length, max_length + 1):
        for i in range(len(sequence) - length + 1):
            segment = sequence[i:i + length]
            if palindrome_check(segment, max_mismatches):
                palindromes.append((i, segment))
    return palindromes

'''
def density():
    densities = []
'''
def palindrome_density(sequence, min_length = 5, max_length = 10, max_mismatches = 2, window_size = 10, step_size = 1):
    densities = []
    for start in range(0, len(sequence) - window_size + 1, step_size):
        window = sequence[start:start + window_size]
        palindromes = find_palindromes(window, min_length = min_length, max_length = max_length, max_mismatches = max_mismatches)
        density = len(palindromes) / window_size
        densities.append((start, density))
    return densities


test = "GAATTCGATATCGAATTC"
result = find_palindromes(test)
print(result)

densities = palindrome_density(test)
print(densities)


def read_fasta(filename):
    sequences = {}
    with open(filename) as f:
        seq_id = None
        seq_lines = []
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if seq_id is not None:
                    sequences[seq_id] = ''.join(seq_lines)
                seq_id = line[1:].split()[0]
                seq_lines = []
            else:
                seq_lines.append(line.upper())
        if seq_id is not None:
            sequences[seq_id] = ''.join(seq_lines)
    return sequences



def density_to_bedgraph(fasta_dict, output_bed, window_size = 1000, step_size = 200, min_length = 5, max_length = 10, max_mismatches = 1):
    with open(output_bed, "w") as out:
        for chrom, seq in fasta_dict.items():
            densities = palindrome_density(seq, min_length, max_length, max_mismatches, window_size, step_size)

            for start, density in densities:
              if density == 0:
                continue
              end = start + window_size
              out.write(chrom + "\t" + str(start) + "\t" + str(end) + "\t" + "{:.6f}".format(density) + "\n")


fasta_file = "genome.fna"
bedgraph_file = "palindrome_density.bedgraph"


fasta_dict = read_fasta(fasta_file)
density_to_bedgraph(fasta_dict, bedgraph_file, window_size = 10, step_size = 1, min_length = 4, max_length = 6, max_mismatches = 1)
