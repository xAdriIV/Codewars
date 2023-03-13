def abbrev_name(name):
    oupt = name[0]
    for i in range(1, len(name)):
        if name[i - 1] == ' ':
            oupt += name[i]
    oupt = oupt.upper()
    return '.'.join(oupt)