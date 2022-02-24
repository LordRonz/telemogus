from itertools import groupby


def sus_in_string(s: str) -> bool:
    return "sus" in "".join(c for c, _ in groupby(s.lower()))
