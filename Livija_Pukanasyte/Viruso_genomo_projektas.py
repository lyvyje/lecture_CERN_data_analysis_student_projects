
import sys, os, re
import matplotlib.pyplot as plt
import numpy as np
import math
import re
import ctypes
from collections import Counter
import collections
from scipy.stats import entropy


with open("clx4rdrp.txt", "r") as file:
    valid = set("ACGT")
    s = file.read()
    for line in s:
        s = s.replace('\n', '')
    # print(s)


#sita vieta sutvarko teksta ir pavercia i substringus sekas

cleanstring = re.sub(r'[^ATGC>]', '', s)  #characters we want to replace, characters get raplaced to this, string
cleanstring = re.sub(r'[^ATGC>]', '>', s)
cleanstring = re.sub(r'>[A-Za-z]{1,3}>', '', cleanstring)  # \w reiskia bet kokia raidę 
cleanstring = re.sub(r'[^ATGC>]', '', cleanstring)  #characters we want to replace, characters get raplaced to this, string
cleanstring = re.sub(r'>+', '>', cleanstring)

substrings = cleanstring.split(">")
substrings = [x for x in substrings if x.strip()]
# print(substrings)

#sita vieta suteikia kintamuosius substringams

sequence_dictionary = {}

for i in range(len(substrings)):
    key = f"seq{i}"   # dynamic key name
    value = substrings[i]   # dynamic value from your list
    sequence_dictionary[key] = value

for name, seq in sequence_dictionary.items():
    # print(name, "=", seq)


# #we will use this to access the sequence from the dictionary
#     seq0 = sequence_dictionary["seq0"]
#     seq1 = sequence_dictionary["seq1"]
# print(seq0)


#Cia prasideda seku sulyginimas

 seq0 = sequence_dictionary["seq0"]
 seq1 = sequence_dictionary["seq1"]


def create_scoring_matrix(seq0, seq1, match_score=1, mismatch_score=-1, gap_score=-1):
    n = len(seq0) + 1
    m = len(seq1) + 1
    score_matrix = np.zeros((n, m))

    # Initialize the scoring matrix
    for i in range(n):
        score_matrix[i][0] = gap_score * i
    for j in range(m):
        score_matrix[0][j] = gap_score * j

    return score_matrix

def fill_scoring_matrix(score_matrix, seq0, seq1, match_score=1, mismatch_score=-1, gap_score=-1):
    for i in range(1, len(seq0) + 1):
        for j in range(1, len(seq1) + 1):
            match = score_matrix[i-1][j-1] + (match_score if seq0[i-1] == seq1[j-1] else mismatch_score)
            delete = score_matrix[i-1][j] + gap_score
            insert = score_matrix[i][j-1] + gap_score
            score_matrix[i][j] = max(match, delete, insert)

def traceback(score_matrix, seq0, seq1, gap_score=-1):
    aligned_seq0 = []
    aligned_seq1 = []
    i, j = len(seq0), len(seq1)

    while i > 0 or j > 0:
        current_score = score_matrix[i][j]
        if i > 0 and j > 0 and current_score == score_matrix[i-1][j-1] + (1 if seq0[i-1] == seq1[j-1] else -1):
            aligned_seq0.append(seq0[i-1])
            aligned_seq1.append(seq1[j-1])
            i -= 1
            j -= 1
        elif i > 0 and current_score == score_matrix[i-1][j] + gap_score:
            aligned_seq0.append(seq0[i-1])
            aligned_seq1.append('-')
            i -= 1
        else:
            aligned_seq0.append('-')
            aligned_seq1.append(seq1[j-1])
            j -= 1

    return ''.join(reversed(aligned_seq0)), ''.join(reversed(aligned_seq1))

def needleman_wunsch(seq0, seq1):
    score_matrix = create_scoring_matrix(seq0, seq1)
    fill_scoring_matrix(score_matrix, seq0, seq1)
    aligned_seq0, aligned_seq1 = traceback(score_matrix, seq0, seq1)
    return aligned_seq0, aligned_seq1


if __name__ == "__main__":

    aligned_seq0, aligned_seq1 = needleman_wunsch(seq0, seq1)
    # print("Aligned Sequences:")
    # print(aligned_seq0)
    # print(aligned_seq1)

#Cia prasideda Shannon entropijos skaiciavimai

def estimate_shannon_entropy(sequence):
    """
    Calculates the Shannon entropy of a DNA sequence.
    """
    counts = collections.Counter(sequence)                 # Count A, C, G, T
    dist = [v/sum(counts.values()) for v in counts.values()]  # Convert to probability distribution
    return entropy(dist, base=2)                            # Shannon entropy in bits

# --- Example usage: calculate entropy for each substring ---
for name, seq in sequence_dictionary.items():
    ent = estimate_shannon_entropy(seq)
    print(f"{name}: Shannon entropy = {ent:.4f}")

# --- Example: align first two sequences and calculate entropy ---
aligned_seq0, aligned_seq1 = needleman_wunsch(seq0, seq1)
entropy_seq0 = estimate_shannon_entropy(aligned_seq0.replace('-', ''))  # ignore gaps for entropy
entropy_seq1 = estimate_shannon_entropy(aligned_seq1.replace('-', ''))
print("\nAligned sequences entropy:")
print(f"seq0: {entropy_seq0:.4f}")
print(f"seq1: {entropy_seq1:.4f}")