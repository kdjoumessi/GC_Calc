def calc_gc_content(seq):
    """ count the number of G and C on this sequence %
    """
    if len(seq) == 0:
        return 0.0
    gc_count = seq.upper().count("C") + seq.upper().count("G")
    gc_content = gc_count / len(seq) * 100

    return gc_content

