def reverse(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    rev = ''
    for base in reversed(seq):
        rev += complement[base]
    return rev


def palindrome_check(seq, max_mismatches = 1):
    rev = reverse(seq)
    mismatches = 0
    for i in range(len(seq)):
        if seq[i] != rev[i]:
            mismatches += 1
            if mismatches > max_mismatches:
               return False
    return True


def find_palindromes(sequence, min_length = 5, max_length = 10, max_mismatches = 1):
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

test = "GAATTCGATATCGAATTC"
result = find_palindromes(test)
print(result)