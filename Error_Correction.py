__author__ = 'Graham'


def correct(inlist):
    sequence_list = []
    loners = []
    error_list = []
    for read in inlist:
        sequence_list.append(read.seq)
    for sequence in sequence_list:
        if sequence_list.count(sequence) == 1:
            if sequence.reverse_complement() not in sequence_list:
                loners.append(sequence_list.pop(sequence_list.index(sequence)))
    for sequence in loners:
        for other_sequence in sequence_list:
            if hamming_dist(sequence, other_sequence) == 1:
                print sequence + '->' + other_sequence
                error_list.append(sequence + '->' + other_sequence)
                break
            elif hamming_dist(sequence, other_sequence.reverse_complement()) == 1:
                print sequence + '->' + other_sequence.reverse_complement()
                error_list.append(sequence + '->' + other_sequence)
                break
    for item in error_list:
        if error_list.count(item) > 1:
            print 'X' * 50


def hamming_dist(seq1,seq2):
    distance = 0
    for base in range(len(seq1)):
        if seq1[base] != seq2[base]:
            distance += 1
    return distance

