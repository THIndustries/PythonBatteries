def luhn_algorithm(nums):
    curr_nums = [int(i) for i in str(nums)]
    result = []
    for i, v in enumerate(curr_nums):
        if i % 2 == 0:
            if v * 2 > 9:
                result.append(v*2 - 9)
            else:
                result.append(v*2)
        else:
            result.append(v)

    return sum(result) % 10 == 0


print(luhn_algorithm(2553514623369426))