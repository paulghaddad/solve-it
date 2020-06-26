# Time: O(n)
# Space: O(n)

def urlify(s, str_len):
    s_arr = list(s)
    num_spaces = 0
    for i in range(0, str_len):
        if s_arr[i] == ' ':
            num_spaces += 1

    r_pt = str_len + num_spaces*2 - 1
    l_pt = str_len - 1

    for i in range(l_pt, -1, -1):
        if s_arr[l_pt] == ' ':
            s_arr[r_pt-2:r_pt+1] = "%", "2", "0"

            l_pt -= 1
            r_pt -= 3
        else:
            s_arr[r_pt] = s_arr[l_pt]
            l_pt -= 1
            r_pt -= 1

    return ''.join(s_arr)
