import re
data = open('input.txt').read().splitlines()
snafu_numbers = [list(x) for x in data]


def add_snafu_digits(dig_1, dig_2):
    if len(re.findall(r'\d+', dig_1)) > 0:
        if len(re.findall(r'\d+', dig_2)) > 0:
            maybe_ans = int(dig_1) + int(dig_2)
            if maybe_ans <= 2:
                return [str(maybe_ans), '0']
            if maybe_ans == 3:
                return ['=', '1']
            if maybe_ans == 4:
                return ['-', '1']
        maybe_ans = int(dig_1)
        if dig_2 == '-':
            maybe_ans = maybe_ans - 1
        if dig_2 == '=':
            maybe_ans = maybe_ans - 2
        if maybe_ans >= 0:
            return [str(maybe_ans), '0']
        if maybe_ans == -1:
            return ['-', '0']
        if maybe_ans == -2:
            return ['=', '0']
    if len(re.findall(r'\d+', dig_2)) > 0:
        maybe_ans = int(dig_2)
        if dig_1 == '-':
            maybe_ans = maybe_ans - 1
        if dig_1 == '=':
            maybe_ans = maybe_ans - 2
        if maybe_ans >= 0:
            return [str(maybe_ans), '0']
        if maybe_ans == -1:
            return ['-', '0']
        if maybe_ans == -2:
            return ['=', '0']
    if dig_1 == '-' and dig_2 == '-':
        return ['=', '0']
    if (dig_1 == '-' and dig_2 == '=') or (dig_2 == '-' and dig_1 == '='):
        return ['2', '-']
    if dig_1 == '=' and dig_2 == '=':
        return ['1', '-']


def add_snafu(snafu_1, snafu_2):
    new_snafu = []
    carry = '0'
    snafu_1.reverse()
    snafu_2.reverse()
    length = max(len(snafu_1), len(snafu_2))
    while len(snafu_1) < length:
        snafu_1.append('0')
    while len(snafu_2) < length:
        snafu_2.append('0')
    print(snafu_1)
    print(snafu_2)
    for i, j in zip(snafu_1, snafu_2):
        dig_sum = add_snafu_digits(i, j)
        dig_sum_with_carried = add_snafu_digits(dig_sum[0], carry)
        carry_sum = add_snafu_digits(dig_sum_with_carried[1], dig_sum[1])
        new_snafu.append(dig_sum_with_carried[0])
        carry = carry_sum[0]
    if carry != '0':
        new_snafu.append(carry)
    new_snafu.reverse()
    return new_snafu


ans = ['0']
for snafu in snafu_numbers:
    ans = add_snafu(ans, snafu)
    print(ans)
ans_str = ''
for snafu_char in ans:
    ans_str += snafu_char
print(ans_str)
