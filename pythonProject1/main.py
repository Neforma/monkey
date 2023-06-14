def char_count(s):
    count_for_ops = 0
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            count_for_ops += 1
            if sym == sub_sym:
                counter += 1
        print(f'количество "{sym}" = {counter} ')
    print(count_for_ops)

char_count('aabc')