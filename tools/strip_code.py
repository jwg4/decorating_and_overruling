def clean_line(line):
    if not line.rstrip():
        return line
    if line.startswith(">>>"):
        return line[4:]
    if line.startswith("..."):
        return line[4:]
    return None

def clean_file(ifile, ofile):
    with open(ifile) as i:
        with open(ofile, 'w') as o:
            for l in i.readlines():
                out = clean_line(l)
                if out is not None:
                    o.write(out)