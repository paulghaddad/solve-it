import functools, operator


def reverse(text=""):
    # Approach 1:

    # reversed_text = ''
    #
    # for _, letter in reversed(list(enumerate(text))):
    #     reversed_text += letter
    #
    # return reversed_text

    # Approach 2

    return functools.reduce(operator.concat, reversed(list(text)), "")
