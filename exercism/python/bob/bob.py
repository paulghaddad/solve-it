SHOUTING_QUESTION_RESPONSE = "Calm down, I know what I'm doing!"
SHOUTING_RESPONSE = 'Whoa, chill out!'
QUESTION_RESPONSE = 'Sure.'
SILENCE_RESPONSE = 'Fine. Be that way!'
DEFAULT_RESPONSE = 'Whatever.'


def response(hey_bob):
    hey_bob = hey_bob.strip()
    is_question = hey_bob.endswith('?')
    is_shouting = hey_bob.isupper()

    if is_shouting and is_question:
        return SHOUTING_QUESTION_RESPONSE
    elif is_shouting:
        return SHOUTING_RESPONSE
    elif is_question:
        return QUESTION_RESPONSE
    elif hey_bob == '':
        return SILENCE_RESPONSE
    else:
        return DEFAULT_RESPONSE
