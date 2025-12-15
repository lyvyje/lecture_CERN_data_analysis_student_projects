import numpy as np
import collections
from scipy.stats import entropy
import re

# ----------------------------
# Functions
# ----------------------------

def read_sequence(file_path):
    """Read a sequence from a file and remove non-ATGC characters."""
    with open(file_path) as f:
        seq = f.read().replace('\n', '').upper()
    seq = re.sub(r'[^ATGC]', '', seq)
    return seq

def create_scoring_matrix(seq0, seq1, match_score=1, mismatch_score=-1, gap_score=-1):
    n, m = len(seq0) + 1, len(seq1) + 1
    score_matrix = np.zeros((n, m))
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
    aligned_seq0, aligned_seq1 = [], []
    i, j = len(seq0), len(seq1)
    while i > 0 or j > 0:
        current_score = score_matrix[i][j]
        if i > 0 and j > 0 and current_score == score_matrix[i-1][j-1] + (1 if seq0[i-1] == seq1[j-1] else -1):
            aligned_seq0.append(seq0[i-1])
            aligned_seq1.append(seq1[j-1])
            i -= 1
            j -= 1
        elif i > 0 and current_score == score_matrix[i-1][j] - 1:
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
    return traceback(score_matrix, seq0, seq1)

def estimate_shannon_entropy(sequence):
    counts = collections.Counter(sequence)
    dist = [v / sum(counts.values()) for v in counts.values()]
    return entropy(dist, base=2)

#allign sequence: 

if __name__ == "__main__":
   
    seq0 = read_sequence("seqdump.txt")
    seq1 = read_sequence("seqdump2.txt")

    # Align sequences
    aligned_seq0, aligned_seq1 = needleman_wunsch(seq0, seq1)

    # Calculate Shannon entropy ignoring gaps
    entropy_seq0 = estimate_shannon_entropy(aligned_seq0.replace('-', ''))
    entropy_seq1 = estimate_shannon_entropy(aligned_seq1.replace('-', ''))


    print("Aligned Sequences:")
    print(aligned_seq0)
    print(aligned_seq1)
    print("\nAligned sequences Shannon entropy:")
    print(f"seq0: {entropy_seq0:.4f}")
    print(f"seq1: {entropy_seq1:.4f}")
