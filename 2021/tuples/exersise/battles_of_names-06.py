def show_me_result(temp):
    print(", ".join(str(x) for x in temp))


number_of_row = int(input())

odd = set()
even = set()

for _ in range(number_of_row):
    name = input()
    temp = sum([ord(i) for i in name]) // (_ + 1)
    if temp & 1:
        odd.add(temp)
    else:
        even.add(temp)

odd_sum = sum(odd)
even_sum = sum(even)


if odd_sum == even_sum:
    result = odd | even
    show_me_result(result)
elif odd_sum > even_sum:
    result = odd - even
    show_me_result(result)
else:
    result = odd ^ even
    show_me_result(result)