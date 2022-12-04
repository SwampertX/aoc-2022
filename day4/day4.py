with open('day4.in', 'r') as f:
    pairs_str = f.read().strip().split('\n')
    pairs = [pair_str.split(',') for pair_str in pairs_str]
    pairs_final = [[tuple(int(i) for i in person.split('-')) for person in pair] for pair in pairs]
    # cnt = 0
    # for pair in pairs_final:
    #     if (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or \
    #         (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]):
    #         cnt += 1
    cnt = 0
    for pair in pairs_final:
        if not (pair[0][1] < pair[1][0] or pair[1][1] < pair[0][0]):
            cnt += 1
    print(cnt)


