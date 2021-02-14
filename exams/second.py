def stock_availability(l, delivery, *args):
    if delivery == 'delivery':
        if args:
            for a in args:
                l.append(a)
    if delivery == 'sell':
        if not args and l:
            l.pop(0)
        elif args and str(args[0]).isdigit():
            l = l[args[0]:]
        elif args and str(args[0]).isalpha():
            l = [i for i in l if i not in args]
    return l









print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 5))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie", "banana"))


'''
['choco', 'vanilla', 'banana', 'caramel', 'berry']
['chocolate', 'vanilla', 'banana', 'cookie', 'banana']
['vanilla', 'banana']
[]
['banana']
['cookie', 'banana']
['chocolate', 'vanilla', 'banana']
'''