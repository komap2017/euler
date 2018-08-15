import numpy as np


def map_seq(seq, f):
    f = np.vectorize(f)
    seq = np.array(seq)
    return f(seq)


def filter_seq(sequence, f):
    return sequence[map_seq(np.array(sequence), f)]


def vertical(seq):
    seq = np.array([np.array(seq)])
    return seq.T


def window_stack(a, step=1, width=1):
    return np.hstack(a[i:1 + i - width or None:step] for i in range(0, width))
