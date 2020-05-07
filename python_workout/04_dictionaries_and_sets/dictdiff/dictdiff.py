def dictdiff(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())

    all_keys = d1_keys.union(d2_keys)
    diff = {}

    for key in all_keys:
        d1_value = d1.get(key)
        d2_value = d2.get(key)
        if d1_value != d2_value:
            diff[key] = [d1_value, d2_value]

    return diff
