FORCED_QUESTION_RESP = "Calm down, I know what I'm doing!"
QUESTION_RESP = "Sure."
YELLING_RESP = "Whoa, chill out!"
SILENCE_RESP = "Fine. Be that way!"
DEFAULT_RESP = "Whatever."


def hey(phrase):
    return (
        forceful_question(phrase) and FORCED_QUESTION_RESP or
        question(phrase) and QUESTION_RESP or
        yelling(phrase) and YELLING_RESP or
        silence(phrase) and SILENCE_RESP or
        DEFAULT_RESP
    )


def question(phrase):
    return phrase.rstrip().endswith("?")


def yelling(phrase):
    return phrase.isupper()


def forceful_question(phrase):
    return question(phrase) and yelling(phrase)


def silence(phrase):
    return not phrase.strip()
