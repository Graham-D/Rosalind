__author__ = 'Graham'

from Hamming_Dist import hamming_dist

def correct(inlist):
    sequence_list = []
    loners = []
    error_list = []
    for read in inlist:
        sequence_list.append(read.seq)
    for sequence in sequence_list:
        if sequence_list.count(sequence) == 1:
            loners.append(sequence_list[sequence_list.index(sequence)])
    for sequence in loners:
        sequence_list.remove(sequence)
    for sequence in loners:
        for other_sequence in sequence_list:
            if hamming_dist(sequence, other_sequence) == 1:
                error_list.append(str(sequence + '->' + other_sequence))
                break
            elif hamming_dist(sequence, other_sequence.reverse_complement()) == 1:
                error_list.append(str(sequence + '->' + other_sequence.reverse_complement))
                break
    return error_list