def reverse(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    rev = ''
    for base in reversed(seq):
        rev += complement[base]
    return rev

def generate_sequences(length, bases = ['A', 'T', 'C', 'G']):
    sequences = ['']
    for i in range(length):
        new_sequences = []
        for seq in sequences:
            for base in bases:
                new_sequences.append(seq + base)
        sequences = new_sequences
    return sequences

def dictionary(min_length = 5, max_length = 10, max_mismatches = 1):
    bases = ['A', 'T', 'C', 'G']
    palindrome_dictionary = {}
    for length in range(min_length, max_length + 1):
        all_sequences = generate_sequences(length, bases)


        for seq in all_sequences:
            rev = reverse(seq)
            if seq == rev:
                palindrome_dictionary[seq] = rev
            else:
                mismatches = 0
                for i in range(len(seq)):
                    if seq[i] != rev[i]:
                        mismatches += 1
                if mismatches <= max_mismatches:
                    palindrome_dictionary[seq] = rev
    return palindrome_dictionary

