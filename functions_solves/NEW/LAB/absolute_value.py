def get_absolute_value(args):
    print([abs(x) for x in args])

data_line = [float(x) for x in input().split()]

get_absolute_value(data_line)