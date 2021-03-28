def complementstrand(fname):
    file = open(fname, 'r')
    sequence = file.read()
    file.close()
    final = ""
    for elem in sequence:
        if elem == "A":
            final = "T" + final
        if elem == "T":
            final = "A" + final
        if elem == "C":
            final = "G" + final
        if elem == "G":
            final = "C" + final
    return final
