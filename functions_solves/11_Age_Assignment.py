def age_assignment(*args, **kwargs):
    result = {}
    for n in args:
        result[n] = kwargs[n[0]]
    return result



print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
