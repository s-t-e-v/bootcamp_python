import random

def generator(text, sep=" ", option=None):
    """
        Splits the text according to sep value and yields the substrings.
    """

    if not isinstance(text, str):
        raise TypeError("Input text must be a string.")
    
    valid_options = ("ordered", "shuffle", "unique", None)
    if option not in valid_options:
         raise ValueError(f"Invalid option. Exected one of {valid_options}")

    substrings = text.split(sep)
 
    if option == "ordered":
        yield from sorted(substrings)
    elif option == "unique":
        yield from dict.fromkeys(substrings).keys()
    elif option == "shuffle":
        tmp = substrings.copy()
        while tmp:
            yield tmp.pop(random.randrange(len(tmp)))
    else:
        yield from substrings

