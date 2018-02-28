import sys
import itertools
from itertools import cycle

verbose = False



p_chars = list(range(32, 126)) + list(range(161, 255))
a_chars = ''.join(chr(i) for i in range(255))

p_chars = list(range(33, 255))
np_chars = ''.join(chr(i) for i in p_chars)

# print(a_chars)
# print(np_chars)


print(len(p_chars))


def read_in_chunks(file_path, n):
    with open(file_path) as fh:
        while True:
            lines = list(itertools.islice(fh, n))
            if lines:
                yield lines
            else:
                break


def np_value(nucleotide, phred_score):

    np_value = (n_mapper[nucleotide] * max_phred) + (ord(phred_score) - 33)
    np_value = chr(np_mapper[np_value])

    return np_value



in_file = 'f.fq'
in_file = 't.fq'
in_file = sys.argv[1]

def shift(line, n):
    return line[-n:] + line[:-n]


n_mapper = {
    'A': 0,
    'T': 1,
    'G': 2,
    'C': 3,
    'N': 4
}

out_file = 's1.bin'
fh = open(out_file, 'w')


for lines in read_in_chunks(in_file, 4):
    # print(lines)
    seq = lines[1].strip()
    score = lines[3].strip()
    # print(lines)
    n_seq = ''
    for i, (n, p) in enumerate(zip(seq, score)):
        nn = n_mapper[n]
        pp = ord(p)
        c_line = shift(np_chars, 41 * nn + pp)
        n_char = c_line[pp]
        # print(i, n, p, ord(p), nn, pp, n_char)
        n_seq += n_char

    if verbose:
        print(lines[1])
        print(lines[3])
        print(n_seq)

    fh.write(n_seq)
    # sys.exit()
        # new_val = np_value(i, n, p)
        # n_seq += new_val

    # identifiers.append(lines[0].strip())
    # n_sequence.append(n_seq)

print('done')
print('')
print('')
