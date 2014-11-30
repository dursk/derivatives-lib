def get_collapse(diff_length):
    collapse = 'monthly'
    if diff_length >= 3:
        collapse = 'quarterly'
        diff_length = diff_length / 3
    return collapse, diff_length
