def reverse(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    rev = ''
    for base in reversed(seq):
        rev += complement[base]
    return rev


def dictionary(sequence, min_length = 5, max_length = 10, max_mismatches = 1):
    palindromeDictionary = {}
    for length in range(min_length, max_length + 1):
        for i in range(len(sequence) - length + 1):
            segment = sequence[i:i + length]
            rev = reverse(segment)
            mismatches = 0
            for i in range(len(segment)):
                if segment[i] != rev[i]:
                    mismatches += 1
            if mismatches <= max_mismatches:
                    palindromeDictionary[segment] = i
    return palindromeDictionary

def findPalindromes(sequence, min_length = 5, max_length = 10, max_mismatches = 1):
    palindromeDictionary = dictionary(sequence, min_length, max_length, max_mismatches)
    palindromes = []
    for seq, position in palindromeDictionary.items():
        palindromes.append((position, seq))
    return palindromes

test = "GAATTCGATATCGAATTC"
result = findPalindromes(test)
print(result)