def read_input():
    """
    Read input
    :return result without zero:
    """
    return [int(x) for x in input().split() if int(x) > 0]


def validate_input_with_twentyfive(scan):
    """
    Second validate input
    :param scan:
    :return list without number divisible by 25 and second f exists:
    """
    temp = []
    for pos, f in enumerate(scan):
        if f > 0 and f % 25:
            temp.append(f)
        if f % 25 == 0:
            if pos + 1 < len(scan):
                scan.pop(pos + 1)
    return temp


def main(males, females) -> int:
    """
    Logic is here
    """
    matches = 0
    while males and females:
        if females[0] == males[-1]:
            matches += 1
            males.pop()
            females.pop(0)
        else:
            females.pop(0)
            males[-1] -= 2
            if males[-1] <= 0:
                males.pop()
    return matches


def show_output(matches, males, females):
    """
    :param matches:
    :param males:
    :param females:
    :return result:
    """
    print(f"Matches: {matches}")
    if not males:
        print("Males left: none")
    else:
        print(f"Males left: {', '.join(str(x) for x in reversed(males))}")
    if not females:
        print("Females left: none")
    else:
        print(f"Females left: {', '.join(str(x) for x in females)}")


males = validate_input_with_twentyfive(read_input())
females = validate_input_with_twentyfive(read_input())
matches = main(males, females)
show_output(matches, males, females)

