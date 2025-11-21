

with open("test_run.txt", "r") as file:
    
 s = file.read()

res = s.splitlines()
print(res)
 

import numpy as np

def create_scoring_matrix(seq1, seq2, match_score=1, mismatch_score=-1, gap_score=-1):
    n = len(seq1) + 1
    m = len(seq2) + 1
    
    score_matrix = np.zeros((n, m))

    # Initialize the scoring matrix
    for i in range(n):
        score_matrix[i][0] = gap_score * i
    for j in range(m):
        score_matrix[0][j] = gap_score * j
    

    return score_matrix

def fill_scoring_matrix(score_matrix, seq1, seq2, match_score=1, mismatch_score=-1, gap_score=-1):
    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            match = score_matrix[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_score)
            delete = score_matrix[i-1][j] + gap_score
            insert = score_matrix[i][j-1] + gap_score
            score_matrix[i][j] = max(match, delete, insert)

def traceback(score_matrix, seq1, seq2, gap_score=-1):
    aligned_seq1 = []
    aligned_seq2 = []
    i, j = len(seq1), len(seq2)

    while i > 0 or j > 0:
        current_score = score_matrix[i][j]
        if i > 0 and j > 0 and current_score == score_matrix[i-1][j-1] + (1 if seq1[i-1] == seq2[j-1] else -1):
            aligned_seq1.append(seq1[i-1])
            aligned_seq2.append(seq2[j-1])
            i -= 1
            j -= 1
        elif i > 0 and current_score == score_matrix[i-1][j] + gap_score:
            aligned_seq1.append(seq1[i-1])
            aligned_seq2.append('-')
            i -= 1
        else:
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[j-1])
            j -= 1

    return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2))

def needleman_wunsch(seq1, seq2):
    score_matrix = create_scoring_matrix(seq1, seq2)
    fill_scoring_matrix(score_matrix, seq1, seq2)
    aligned_seq1, aligned_seq2 = traceback(score_matrix, seq1, seq2)
    return aligned_seq1, aligned_seq2

if __name__ == "__main__":
    aligned_seq1, aligned_seq2 = needleman_wunsch(res[0],res[1])
    print("Aligned Sequences:")
    print(aligned_seq1)
    print(aligned_seq2)
