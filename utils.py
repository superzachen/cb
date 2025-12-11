import pathlib

def load_eng_dict() -> set:
    myset = set()
    p = pathlib.Path("./words.txt")
    for line in p.read_text().split("\n"):
        myset.add(line.lower())
    return myset
