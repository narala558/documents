#!/usr/bin/env python3


import os
import sys
import itertools

from Levenshtein import distance
from cluster import HierarchicalClustering


in_file = sys.argv[1]
# in_file ='t.fq'

out_file = in_file + '.bin'

out = open(out_file, 'wb')
max_phred = 60
n_mapper = {
    'A': 0,
    'T': 1,
    'G': 2,
    'C': 3,
    'N': 4
}

np_mapper = list(range(32, 126)) + list(range(161, 371))


def read_in_chunks(file_path, n):
    with open(file_path) as fh:
        while True:
            lines = list(itertools.islice(fh, n))
            if lines:
                yield lines
            else:
                break


def nucleotide_filter(seq):
    """
    Check for non nucleotide(other than A,C,T,G,N) and convert to N
    """
    valid_set = set('ACTGN')
    if set(seq).issubset(valid_set):
        return seq
    else:
        new_seq = ''.join(i if i in valid_set else 'N' for i in seq)
        return new_seq


def np_value(nucleotide, phred_score):

    np_value = (n_mapper[nucleotide] * max_phred) + (ord(phred_score) - 33)
    np_value = chr(np_mapper[np_value])

    return np_value


identifiers = []
n_sequence = []


for lines in read_in_chunks(in_file, 4):
    seq = lines[1].strip()
    score = lines[3].strip()
    # print(lines)
    seq = nucleotide_filter(seq)
    n_seq = ''
    for i, j in zip(seq, score):
        new_val = np_value(i, j)
        n_seq += new_val

    identifiers.append(lines[0].strip())


# print(identifiers)
# print(n_sequence)
# print(n_sequence)
n_sequence = zip(*n_sequence)
n_sequence = [''.join(i) for i in n_sequence]
n_sequence.sort(key=len, reverse=True)

p_size = 0
new_seq = []
chunk = []
for seq in n_sequence:
    size = len(seq)
    if size == p_size:
        new_seq.append(seq)
    else:
        p_size = size
        if chunk:
            cl = HierarchicalClustering(chunk, lambda x, y: distance(x, y))
            cl.getlevel(1)
            new_seq += cl
            print(new_seq)
            chunk = []

print(len(n_sequence))
print(len(identifiers))
out.write(bytes(''.join(identifiers), 'UTF-8'))
out.write(bytes('\n', 'UTF-8'))
out.write(bytes('\n'.join(n_sequence), 'UTF-8'))
out.write(bytes('\n', 'UTF-8'))
out.close()

in_size = os.path.getsize(in_file)
out_size = os.path.getsize(out_file)


print((in_size - out_size)*100/(in_size * 1.0))
