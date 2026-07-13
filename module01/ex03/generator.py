import random

def generator(text, sep=" ", option=None):
    """
        Splits the text according to sep value and yields the substrings.
    """

    if type(text) != str:
        print("ERROR")
        return

    substrings = text.split(sep)
    new_substrs = []

    nb_substrs = len(substrings)

    if option == "shuffle":
        new_substrs = [substrings.pop(random.randrange(len(substrings))) for _ in range(nb_substrs)]
    elif option == "unique":
        new_substrs = dict.fromkeys(substrings, None).keys()
    elif option == "ordered":
        new_substrs = sorted(substrings)
    elif option == None:
        new_substrs = substrings
    else:
        raise ValueError("Unknown option")

    for s in new_substrs:
        yield s

