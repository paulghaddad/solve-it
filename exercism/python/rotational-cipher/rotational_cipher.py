from string import ascii_lowercase as lower, ascii_uppercase as upper

def rotate(text, key):
    key = key % 26
    rotated_lower = lower[key:] + lower[:key]
    rotated_upper = upper[key:] + upper[:key]

    # Approach 1: pass in two arguments to maketrans and allow the function to
    # create the mapping
    rotation_mapping = str.maketrans(lower+upper, rotated_lower+rotated_upper)
    return text.translate(rotation_mapping)

    # Approach 2: Create a dict of the mappings using zip and pass that in to
    # maketrans as a single argument
    rotated_char_mapping = dict(zip(lower+upper, rotated_lower+rotated_upper))
    rotation_translation = str.maketrans(rotated_char_mapping)

    return text.translate(rotation_translation)
