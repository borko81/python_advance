def get_input():
    return [int(x) for x in input().split(', ')]

customers = get_input()
taxi = get_input()
total_time = 0


def validate(cust, tax):
    return cust <= tax


while customers and taxi:
    cur_customer = customers[0]
    cur_taxi = taxi[-1]
    if validate(cur_customer, cur_taxi):
        total_time += cur_customer
        customers.pop(0)
        taxi.pop()
    else:
        taxi.pop()


def main():
    if not customers:
        print("All customers were driven to their destinations")
        print(f"Total time: {total_time} minutes")
    else:
        print("Not all customers were driven to their destinations")
        print(f"Customers left: {', '.join(str(x) for x in customers)}")


main()