string = input().split(', ')

print(', '.join(['{first_str} -> {first_str_len}'.format(first_str=s, first_str_len=len(s)) for s in string]))