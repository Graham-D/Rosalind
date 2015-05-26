__author__ = 'Graham'


def overlaps(infile):
    list_edges = []
    for fragment in infile:
        for other_fragment in infile:
            if fragment.seq[-3:] == other_fragment.seq[0:3] and fragment != other_fragment:
                list_edges.append(str(fragment.id + ' ' + other_fragment.id))

    for entry in list_edges:
            print entry