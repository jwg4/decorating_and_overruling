def clean_line(line):
    if not line.rstrip():
        return line
    if line.startswith(">>>"):
        return line[4:]
    if line.startswith("..."):
        return line[4:]
    return None