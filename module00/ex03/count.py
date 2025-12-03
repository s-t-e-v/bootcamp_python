import sys
import string


def text_analyzer(text=""):
    """This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    if not isinstance(text, (str, type(None))):
        print("AssertionError: argument is not a string")
        return
    if not text:
        print("What is the text to analyze?")
        text = input()
    printable_characters = 0
    upper_cases = 0
    lower_cases = 0
    punctuations = 0
    spaces = 0
    for c in text:
        if c.isprintable():
            printable_characters += 1
        if c.isupper():
            upper_cases += 1
        elif c.islower():
            lower_cases += 1
        elif c == " ":
            spaces += 1
        elif c in string.punctuation:
            punctuations += 1
    print(f"""\
The text contains {printable_characters} printable character(s):
- {upper_cases} upper letter(s)
- {lower_cases} lower letter(s)
- {punctuations} punctuation mark(s)
- {spaces} space(s)""")


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) > 1:
        print("AssertionError: too many arguments")
        sys.exit()
    text = args[0] if args else ""
    text_analyzer(text)
