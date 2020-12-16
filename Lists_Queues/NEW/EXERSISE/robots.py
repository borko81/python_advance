import datetime

line = input()
free_robots = []
work_robots = []


def convert_time(time, seconds):
    up_second = 1

    h, m, s = map(int, time.split(':'))
    new_time = str(datetime.datetime(2000, 1, 1, h, m, s) + datetime.timedelta(seconds=up_second)).split(' ')[-1]
    return new_time


def convert_time2(time, seconds):
    up_second = seconds

    h, m, s = map(int, time.split(':'))
    new_time = str(datetime.datetime(2000, 1, 1, h, m, s) + datetime.timedelta(seconds=up_second)).split(' ')[-1]
    return new_time


for l in line.split(';'):
    free_robots.append(l)

time = input()
count = 0
l = len(free_robots)

while True:
    command = input()
    if command == 'End':
        break

    if free_robots:
        temp = free_robots.pop(0)
        work_robots.append(temp)
        name, check = temp.split('-')
        time = convert_time(time, 0)
        print(f"{name} - {command} [{time}]")
    else:
        temp = work_robots.pop()
        name, check = temp.split('-')
        time = convert_time2(time, int(check))
        work_robots.insert(0, temp)
        print(f"{name} - {command} [{time}]")


