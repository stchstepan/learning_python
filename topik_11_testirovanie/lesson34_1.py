def get_formated_name(first, last, second=''):
    if second:
        full_name = f"{last} {first} {second}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()