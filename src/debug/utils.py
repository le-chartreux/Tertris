"""
File that contains the declaration of some debug utilities
"""


def print_in_output_dot_txt(text: str) -> None:
    """
    Appends <text> at the end of output.txt

    :param text: text to append
    """
    with open("output.txt", "a") as output_dot_txt:
        output_dot_txt.write(text + '\n')
