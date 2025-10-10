def reverse(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    rev = ''
    for base in reversed(seq):
        rev += complement[base]
    return rev

def generateSequences(length, bases=['A', 'T', 'C', 'G']):
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
    palindromeDictionary = {}
    for length in range(min_length, max_length + 1):
        allSequences = generateSequences(length, bases)


        for seq in allSequences:
            rev = reverse(seq)
            if seq == rev:
                palindromeDictionary[seq] = rev
            else:
                mismatches = 0
                for i in range(len(seq)):
                    if seq[i] != rev[i]:
                        mismatches += 1
                if mismatches <= max_mismatches:
                    palindromeDictionary[seq] = rev
    return palindromeDictionary

