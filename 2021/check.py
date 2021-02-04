"""
Rerolled infinity question with change user name
"""

common = {
    '1': "User One",
    '2': 'User Two'
}


def show_print(user, answer):
    print(f'{common.get(user)}: {answer}')


def get_answer_from_user(user):
    answer = input("Enter some number :")
    show_print(user, answer)
    check_user = '2' if user == '1' else '1'
    return get_answer_from_user(check_user)


def rerolled_infinity():
    while True:
        get_answer_from_user('1')


if __name__ == '__main__':
    rerolled_infinity()