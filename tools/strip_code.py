def clean_line(line):
    if not line.rstrip():
        return line
    if line.startswith(">>>"):
        return line
    return None