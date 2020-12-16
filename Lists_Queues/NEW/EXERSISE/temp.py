import datetime


def convert_time(time, seconds):
    up_second = 1 + seconds

    h, m, s = map(int, time.split(':'))
    new_time = str(datetime.datetime(2000, 1, 1, h, m, s) + datetime.timedelta(seconds=up_second)).split(' ')[-1]
    print(new_time)


convert_time('8:00:00', seconds=0)